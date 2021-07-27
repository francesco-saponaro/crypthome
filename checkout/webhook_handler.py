from django.http import HttpResponse

# Each time an event occurs on Stripe, it sends webhooks
# we can listen for.


# Handle stripe webhooks.
class StripeWH_Handler:

    # I can create instances of this class by passing in the request.
    def __init__(self, request):
        self.request = request

    # Handle a generic/unknown/unexpected webhook event.
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    # Handle payment intent succeeded.
    # It will be sent each time the user completes a payment process.
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    # Handle payment intent failing.
    # It will be sent each time the user payment fails.
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200
        )
