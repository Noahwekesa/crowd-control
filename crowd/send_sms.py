from __future__ import print_function
import africastalking

# SANDBOX_API_KEY = "dcb1d194cd520eaf98117195fbc9a1232e372d22eb0a938ca913b30e30ca80ff"


# works with both python 2 and 3


class SMS:
    def __init__(self):
        self.username = "sandbox"
        self.api_key = (
            "dcb1d194cd520eaf98117195fbc9a1232e372d22eb0a938ca913b30e30ca80ff"
        )

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+254721914166", "+254741642501"]

        # Set your message
        message = "Area A is over crowded. Please control the crowd."

        # Set your shortCode or senderId
        # sender = "shortCode or senderId"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print("Encountered an error while sending: %s" % str(e))


SMS().send()
