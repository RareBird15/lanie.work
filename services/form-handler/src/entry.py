# Copyright (c) 2026 Lanie
"""Cloudflare worker for contact form with Turnstile verification."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Protocol
from urllib.parse import urlencode

if TYPE_CHECKING:
    from workers import Request, Response, WorkerEntrypoint
    from workers import (
        fetch as workers_fetch,  # type: ignore[import-not-found]
    )
else:
    from workers import Request, Response, WorkerEntrypoint
    from workers import fetch as workers_fetch


class Env(Protocol):
    """Protocol for environment variables."""

    BREVO_API_KEY: str
    TURNSTILE_SECRET_KEY: str


class Default(WorkerEntrypoint):
    """Main entrypoint for the Worker."""

    async def fetch(self, request: Request) -> Response:
        """Handle incoming HTTP requests with spam protection.

        Returns:
            Response: HTTP response containing success or error details.

        """
        env: Env = self.env  # type: ignore[assignment]

        if request.method != "POST":
            return Response("Method Not Allowed", status=405)

        try:
            form_data = await request.form_data()

            # 1. Honeypot check
            # If a bot fills out this hidden field, reject the request immediately.
            honeypot = str(form_data.get("website_url") or "").strip()
            if honeypot:
                return Response("Spam detected.", status=400)

            # 2. Extract the Turnstile token
            token = str(form_data.get("cf-turnstile-response") or "").strip()
            if not token:
                return Response("Spam check missing.", status=400)

            # 3. Verify the token with Cloudflare
            verify_body = urlencode(
                {
                    "secret": env.TURNSTILE_SECRET_KEY,
                    "response": token,
                },
            )

            verify_res = await workers_fetch(
                "https://challenges.cloudflare.com/turnstile/v0/siteverify",
                method="POST",
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                body=verify_body,
            )

            if not verify_res.ok:
                return Response("Spam check could not be verified.", status=502)

            verify_data = await verify_res.json()
            if not isinstance(verify_data, dict) or not verify_data.get("success"):
                return Response("Spam check failed.", status=403)

            # 4. Extract and normalize form fields
            user_name = str(form_data.get("name") or "Anonymous").strip()[:100]
            user_email = str(form_data.get("email") or "").strip()[:254]
            user_subject = str(form_data.get("subject") or "No Subject").strip()[:150]
            user_message = str(form_data.get("message") or "").strip()[:5000]

            if not user_message:
                return Response("Message is required.", status=400)

            if not is_valid_basic_email(user_email):
                return Response("Please provide a valid email address.", status=400)

            # 5. Sender blocking
            banned_emails = {
                "no.reply.willyfrangois@gmail.com",
            }

            if user_email.lower() in banned_emails:
                return Response("Sender blocked.", status=403)

            # 6. Keyword filtering
            banned_keywords = {
                "t.me/",
                "wa.me/",
                "million messages",
            }

            message_lower = user_message.lower()
            subject_lower = user_subject.lower()

            for keyword in banned_keywords:
                if keyword in message_lower or keyword in subject_lower:
                    return Response("Message blocked by content filter.", status=403)

            # 7. Send email through Brevo
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

            if not brevo_res.ok:
                return Response(
                    "Email service error. Please try again later.",
                    status=502,
                )

            return Response("Success! Your message was sent.", status=200)

        except Exception:
            return Response(
                "Internal error. Please try again later.",
                status=500,
            )


def is_valid_basic_email(email: str) -> bool:
    """Return True if an email address is plausibly valid.

    This is intentionally basic. Brevo will still do stricter validation.
    """
    if not email:
        return False

    if len(email) > 254:
        return False

    if "@" not in email:
        return False

    local_part, _, domain = email.partition("@")

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    return not any(char.isspace() for char in email)
