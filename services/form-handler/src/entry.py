# Copyright (c) 2026 Lanie
"""Cloudflare worker for contact form with Turnstile verification."""

import json
from typing import TYPE_CHECKING, Protocol
from urllib.parse import urlencode

if TYPE_CHECKING:
    from workers import fetch as workers_fetch, Request, Response, WorkerEntrypoint  # type: ignore[import-not-found]  # noqa: I001
else:
    from workers import fetch as workers_fetch, Request, Response, WorkerEntrypoint  # noqa: I001


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

        if request.method != 'POST':
            return Response('Method Not Allowed', status=405)

        try:
            form_data = await request.form_data()

            # 1. Honeypot Check
            # If a bot fills out this hidden field, reject the request immediately.
            honeypot = form_data.get('website_url')
            if honeypot:
                return Response('Spam detected.', status=400)

            # 2. Extract the Turnstile token
            token = form_data.get('cf-turnstile-response')
            if not token:
                return Response('Spam check missing.', status=400)
            token = str(token)

            # 3. Verify the token with Cloudflare
            verify_body = urlencode(
                {'secret': env.TURNSTILE_SECRET_KEY, 'response': token},
            )

            verify_res = await workers_fetch(
                'https://challenges.cloudflare.com/turnstile/v0/siteverify',
                method='POST',
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                body=verify_body,
            )

            verify_data = await verify_res.json()
            if not verify_data.get('success'):
                return Response('Spam check failed.', status=403)

            # 4. Extract form fields
            user_name = str(form_data.get('name') or 'Anonymous')
            user_email = str(form_data.get('email') or 'No Email')
            user_subject = str(form_data.get('subject') or 'No Subject')
            user_message = str(form_data.get('message') or 'No Message')

            # 5. Domain and Email Blocking
            banned_emails = ['no.reply.willyfrangois@gmail.com']
            if user_email.lower() in banned_emails:
                return Response('Sender blocked.', status=403)

            # 6. Keyword Filtering
            banned_keywords = ['t.me/', 'wa.me/', 'million messages']
            message_lower = user_message.lower()

            for keyword in banned_keywords:
                if keyword in message_lower:
                    return Response('Message blocked by content filter.', status=403)

            # 7. Proceed with email logic
            email_payload = {
                'sender': {
                    'name': 'Lanie: Faith, Tech & Advocacy',
                    'email': 'contact@lanie.work',
                },
                'to': [{'email': 'lanie@lanie.work'}],
                'replyTo': {'email': user_email, 'name': user_name},
                'subject': f'[{user_subject}] Message from {user_name}',
                'textContent': (
                    f'Name: {user_name}\n'
                    f'Email: {user_email}\n\n'
                    f'Subject: {user_subject}\n\n'
                    f'Message:\n{user_message}'
                ),
            }

            await workers_fetch(
                'https://api.brevo.com/v3/smtp/email',
                method='POST',
                headers={
                    'accept': 'application/json',
                    'content-type': 'application/json',
                    'api-key': env.BREVO_API_KEY,
                },
                body=json.dumps(email_payload),
            )

            return Response('Success! Your message was sent.', status=200)

        except (TypeError, ValueError, KeyError, RuntimeError) as e:
            return Response(f'Internal Error: {e!s}', status=500)
