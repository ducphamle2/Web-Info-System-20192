from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

import sys


class PayPalClient:
    def __init__(self):
        self.client_id = "AZSM8h2MflxGM0iBCmrJMyTJFtlIn4WIwZS-J6OgU6VLX0S4lgNp8xhVv1RTwL5xfzjw6jRqHdT7iOrr"
        self.client_secret = "EMiJ2RjZa3iXHrTTiQhT2_RdzCQK-_IEzQV9S17EmuvEbOdJkMsbdzZuz4vR2aSsQYcvGchIxO4v2z4Z"

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)
