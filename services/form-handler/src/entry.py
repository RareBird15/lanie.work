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
        """Handle incoming HTTP requests with spam protection."""
        env: Env = self.env  # type: ignore

        if request.method != 'POST':
            return Response('Method Not Allowed', status=405)

        try:
            form_data = await request.form_data()

            # 1. Extract the Turnstile token
            token = form_data.get('cf-turnstile-response')
            if not token:
                return Response('Spam check missing.', status=400)
            token = str(token)

            # 2. Verify the token with Cloudflare
            # We use a URL-encoded body as required by the Turnstile API
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

            # 3. If human, proceed with email logic
            user_name = form_data.get('name') or 'Anonymous'
            user_email = form_data.get('email') or 'No Email'
            user_subject = form_data.get('subject') or 'No Subject'
            user_message = form_data.get('message') or 'No Message'
            user_name = str(user_name)
            user_email = str(user_email)
            user_subject = str(user_subject)
            user_message = str(user_message)

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

        except Exception as e:
            return Response(f'Internal Error: {e!s}', status=500)
