# Copyright (c) 2026 Lanie
"""Cloudflare worker for contact form and newsletter subscriptions.

DEPRECATED (July 2026): This Worker is no longer deployed. The contact form
has migrated to Formspree (https://formspree.io/f/mqergapg) and the newsletter
subscribe form has migrated to Buttondown (https://buttondown.com/RareBird15).
The code is preserved here for reference. The deploy workflow has been
restricted to manual dispatch only.
"""

from __future__ import annotations

import importlib
import json
from typing import Protocol
from urllib.parse import urlencode, urlparse

_workers = importlib.import_module("workers")
Request = _workers.Request
Response = _workers.Response
WorkerEntrypoint = _workers.WorkerEntrypoint
workers_fetch = _workers.fetch

SUCCESS_MESSAGE = "Success! Your message was sent."
INTERNAL_ERROR_MESSAGE = "Internal error. Please try again later."
EMAIL_SERVICE_ERROR_MESSAGE = "Email service error. Please try again later."
SPAM_CHECK_FAILED_MESSAGE = "Spam check failed."
MAX_EMAIL_LENGTH = 254
ALLOWED_FORM_CONTENT_TYPES = (
    "application/x-www-form-urlencoded",
    "multipart/form-data",
)

EXPECTED_ACTION = "contact_form"
SUBSCRIBE_ACTION = "newsletter_subscribe"
ALLOWED_HOSTNAMES = {"lanie.work", "www.lanie.work"}

BANNED_EMAILS = {
    "no.reply.willyfrangois@gmail.com",
}

BANNED_KEYWORDS = {
    "t.me/",
    "wa.me/",
    "million messages",
}

MAX_MESSAGE_LINKS = 2

SUBSCRIBE_SUCCESS_MESSAGE = "Success! Check your inbox for a confirmation email."
SUBSCRIBE_ERROR_MESSAGE = "Something went wrong. Please try again later."
SUBSCRIBE_DUPLICATE_MESSAGE = "You're already subscribed!"
SUBSCRIBE_INVALID_EMAIL_MESSAGE = "Please provide a valid email address."


class FormDataLike(Protocol):
    """Protocol for `Request.form_data()` results used by this worker."""

    def get(self, key: str) -> object:
        """Return a submitted form value for the provided key."""


class Env(Protocol):
    """Protocol for environment variables."""

    BREVO_API_KEY: str
    BREVO_LIST_ID: str
    TURNSTILE_SECRET_KEY: str


class Default(WorkerEntrypoint):
    """Main entrypoint for the Worker."""

    async def fetch(self, request: Request) -> Response:
        """Handle incoming HTTP requests with spam protection.

        Routes to the contact form handler or the newsletter subscribe handler
        based on the URL path.

        Returns:
            Response: Result of form validation and delivery.
        """
        env: Env = self.env  # type: ignore[assignment]

        if request.method != "POST":
            return Response("Method Not Allowed", status=405)

        try:
            content_type = (request.headers.get("content-type") or "").lower()
            if not is_allowed_content_type(content_type):
                return fake_success()

            form_data = await request.form_data()
            path = urlparse(request.url).path

            if path == "/api/subscribe":
                return await process_subscription(request, env, form_data)

            return await process_submission(request, env, form_data)
        # Intentionally broad fallback so unexpected runtime errors never leak.
        except Exception:
            return Response(INTERNAL_ERROR_MESSAGE, status=500)


async def process_submission(
    request: Request,
    env: Env,
    form_data: FormDataLike,
) -> Response:
    """Validate and process a contact form submission.

    Returns:
        Response: Success, fixable error, or spam rejection response.
    """
    honeypot = str(form_data.get("website_url") or "").strip()
    if honeypot:
        return fake_success()

    token = str(form_data.get("cf-turnstile-response") or "").strip()
    if not token:
        return Response("Spam check missing.", status=400)

    if not await verify_turnstile(request, env, token):
        return Response(SPAM_CHECK_FAILED_MESSAGE, status=403)

    user_name = str(form_data.get("name") or "Anonymous").strip()[:100]
    user_email = str(form_data.get("email") or "").strip()[:MAX_EMAIL_LENGTH]
    user_subject = str(form_data.get("subject") or "No Subject").strip()[:150]
    user_message = str(form_data.get("message") or "").strip()[:5000]

    validation_error = validate_input(user_email, user_message)
    if validation_error is not None:
        return validation_error

    if should_soft_block(user_email, user_subject, user_message):
        return fake_success()

    was_sent = await send_via_brevo(
        env=env,
        user_name=user_name,
        user_email=user_email,
        user_subject=user_subject,
        user_message=user_message,
    )
    return (
        fake_success()
        if was_sent
        else Response(EMAIL_SERVICE_ERROR_MESSAGE, status=502)
    )


async def verify_turnstile(
    request: Request,
    env: Env,
    token: str,
    expected_action: str = EXPECTED_ACTION,
) -> bool:
    """Return True when Turnstile verification succeeds for this form."""
    remote_ip = request.headers.get("CF-Connecting-IP") or ""
    verify_body = urlencode(
        {
            "secret": env.TURNSTILE_SECRET_KEY,
            "response": token,
            "remoteip": remote_ip,
        },
    )

    verify_res = await workers_fetch(
        "https://challenges.cloudflare.com/turnstile/v0/siteverify",
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        body=verify_body,
    )
    if not verify_res.ok:
        return False

    try:
        verify_data = await verify_res.json()
    except ValueError:
        return False

    if not isinstance(verify_data, dict):
        return False

    if not verify_data.get("success"):
        return False

    if verify_data.get("action") != expected_action:
        return False

    return verify_data.get("hostname") in ALLOWED_HOSTNAMES


def validate_input(user_email: str, user_message: str) -> Response | None:
    """Return a fixable user-facing error response, or None if valid."""
    if not user_message:
        return Response("Message is required.", status=400)

    if not is_valid_basic_email(user_email):
        return Response("Please provide a valid email address.", status=400)

    return None


def is_allowed_content_type(content_type: str) -> bool:
    """Return True when the request content type matches expected form posts."""
    return any(allowed in content_type for allowed in ALLOWED_FORM_CONTENT_TYPES)


def should_soft_block(user_email: str, user_subject: str, user_message: str) -> bool:
    """Return True when a submission looks like spam and should be silently dropped."""
    normalized_email = user_email.lower()
    if normalized_email in BANNED_EMAILS:
        return True

    message_lower = user_message.lower()
    subject_lower = user_subject.lower()

    for keyword in BANNED_KEYWORDS:
        if keyword in message_lower or keyword in subject_lower:
            return True

    if count_links(user_subject) > 0:
        return True

    return count_links(user_message) > MAX_MESSAGE_LINKS


def count_links(text: str) -> int:
    """Count rough link patterns in plain text.

    Returns:
        int: Count of `http://`, `https://`, and `www.` occurrences.
    """
    lowered = text.lower()
    return lowered.count("http://") + lowered.count("https://") + lowered.count("www.")


def fake_success() -> Response:
    """Return a generic success response used for soft spam drops."""
    return Response(SUCCESS_MESSAGE, status=200)


async def send_via_brevo(
    *,
    env: Env,
    user_name: str,
    user_email: str,
    user_subject: str,
    user_message: str,
) -> bool:
    """Send an email through Brevo.

    Returns:
        bool: True when the Brevo API accepts the request.
    """
    email_payload = {
        "sender": {
            "name": "Lanie: Faith, Tech & Advocacy",
            "email": "contact@lanie.work",
        },
        "to": [{"email": "lanie@lanie.work"}],
        "replyTo": {
            "email": user_email,
            "name": user_name,
        },
        "subject": f"[{user_subject}] Message from {user_name}",
        "textContent": (
            f"Name: {user_name}\n"
            f"Email: {user_email}\n\n"
            f"Subject: {user_subject}\n\n"
            f"Message:\n{user_message}"
        ),
    }

    brevo_res = await workers_fetch(
        "https://api.brevo.com/v3/smtp/email",
        method="POST",
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": env.BREVO_API_KEY,
        },
        body=json.dumps(email_payload),
    )
    return bool(brevo_res.ok)


def is_valid_basic_email(email: str) -> bool:
    """Return True if an email address is plausibly valid.

    This is intentionally basic. Brevo will still do stricter validation.
    """
    if not email:
        return False

    if len(email) > MAX_EMAIL_LENGTH:
        return False

    if "@" not in email:
        return False

    local_part, _, domain = email.partition("@")

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    return not any(char.isspace() for char in email)


async def process_subscription(
    request: Request,
    env: Env,
    form_data: FormDataLike,
) -> Response:
    """Validate and process a newsletter subscription request.

    Returns:
        Response: Success, fixable error, or spam rejection response.
    """
    honeypot = str(form_data.get("website_url") or "").strip()
    if honeypot:
        return Response(SUBSCRIBE_SUCCESS_MESSAGE, status=200)

    token = str(form_data.get("cf-turnstile-response") or "").strip()
    if not token:
        return Response("Spam check missing.", status=400)

    if not await verify_turnstile(request, env, token, SUBSCRIBE_ACTION):
        return Response(SPAM_CHECK_FAILED_MESSAGE, status=403)

    user_email = str(form_data.get("email") or "").strip()[:MAX_EMAIL_LENGTH]

    if not is_valid_basic_email(user_email):
        return Response(SUBSCRIBE_INVALID_EMAIL_MESSAGE, status=400)

    if user_email.lower() in BANNED_EMAILS:
        return Response(SUBSCRIBE_SUCCESS_MESSAGE, status=200)

    result = await subscribe_via_brevo(env=env, user_email=user_email)

    if result == "created":
        return Response(SUBSCRIBE_SUCCESS_MESSAGE, status=200)
    if result == "duplicate":
        return Response(SUBSCRIBE_DUPLICATE_MESSAGE, status=200)
    return Response(SUBSCRIBE_ERROR_MESSAGE, status=502)


async def subscribe_via_brevo(*, env: Env, user_email: str) -> str:
    """Add a contact to the newsletter list via the Brevo API.

    Returns:
        str: "created" on success, "duplicate" if already exists, "error" on failure.
    """
    list_id = int(env.BREVO_LIST_ID)
    contact_payload = {
        "email": user_email,
        "listIds": [list_id],
        "updateEnabled": True,
    }

    brevo_res = await workers_fetch(
        "https://api.brevo.com/v3/contacts",
        method="POST",
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "api-key": env.BREVO_API_KEY,
        },
        body=json.dumps(contact_payload),
    )

    if brevo_res.ok:
        return "created"

    # 400 with "already exists" means the contact is already in our account.
    # We need to check if they're already on the list, and add them if not.
    if brevo_res.status == 400:
        # Try adding the contact to the list directly
        add_payload = {"emails": [user_email]}
        add_res = await workers_fetch(
            f"https://api.brevo.com/v3/contacts/lists/{list_id}/contacts/add",
            method="POST",
            headers={
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": env.BREVO_API_KEY,
            },
            body=json.dumps(add_payload),
        )
        if add_res.ok:
            return "duplicate"
    return "error"
