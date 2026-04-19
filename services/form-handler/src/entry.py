"""Cloudflare worker for contact form with Turnstile verification."""

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from js import JSON, fetch  # type: ignore[import-not-found]
    from workers import (  # type: ignore[import-not-found]
        Request,
        Response,
        WorkerEntrypoint,
    )
else:
    from js import JSON, fetch
    from workers import Request, Response, WorkerEntrypoint


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
            form_data = await request.formData()

            # 1. Extract the Turnstile token
            token = form_data.get('cf-turnstile-response')
            if not token:
                return Response('Spam check missing.', status=400)

            # 2. Verify the token with Cloudflare
            # We use a URL-encoded body as required by the Turnstile API
            verify_body = f'secret={env.TURNSTILE_SECRET_KEY}&response={token}'

            verify_res = await fetch(
                'https://challenges.cloudflare.com/turnstile/v0/siteverify',
                {
                    'method': 'POST',
                    'headers': {'Content-Type': 'application/x-www-form-urlencoded'},
                    'body': verify_body,
                },
            )

            verify_data = await verify_res.json()
            if not verify_data.success:
                return Response('Spam check failed.', status=403)

            # 3. If human, proceed with email logic
            user_name = form_data.get('name') or 'Anonymous'
            user_email = form_data.get('email') or 'No Email'
            user_message = form_data.get('message') or 'No Message'

            email_payload = {
                'sender': {
                    'name': 'Lanie: Faith, Tech & Advocacy',
                    'email': 'contact@lanie.work',
                },
                'to': [{'email': 'lanie@lanie.work'}],
                'replyTo': {'email': user_email, 'name': user_name},
                'subject': f'New Message from {user_name}',
                'textContent': (
                    f'Name: {user_name}\n'
                    f'Email: {user_email}\n\n'
                    f'Message:\n{user_message}'
                ),
            }

            await fetch(
                'https://api.brevo.com/v3/smtp/email',
                {
                    'method': 'POST',
                    'headers': {
                        'accept': 'application/json',
                        'content-type': 'application/json',
                        'api-key': env.BREVO_API_KEY,
                    },
                    'body': JSON.stringify(email_payload),
                },
            )

            return Response('Success! Your message was sent.', status=200)

        except Exception as e:
            return Response(f'Internal Error: {e!s}', status=500)
