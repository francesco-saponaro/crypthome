from django.http import HttpResponse

from .models import Order, OrderLineItem
from merch.models import Merch

import json
import time

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
        # Intent with all of customer info into it.
        intent = event.data.object
        # Get from it payment intent id, the bag and the save info
        # preference from the metadata we added earlier on js.
        # And also the billing and shipping details and the total.
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # To ensure the data is in the same for as we want in our
        # database, let's replace any empty string with a value of
        # "none".
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Let's assume the order doesn't exist.
        order_exists = False
        # If the checkout view is slow for some reason and hasn't
        # created the order by the time we get the webhook from
        # stripe, the webhook handler will create another order since
        # it didnt find any order. And once the view finally finishes it
        # will result in the same order being added twice to the database.
        # Therefore let's introduce a delay by letting the webhook handler
        # attempt to find the order 5 times from the database and wait 1 
        # second each time, before giving up and creating the order itself.
        attempt = 1
        while attempt <= 5:
            try:
                # Let's try get the order using the information from
                # the payment intent.
                # Using the "exact" lookup field to make it an exact match
                # and case insensitive.
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # If the order is found (exists) we'll set the order exists
                # variable to true, and break the loop.
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        # If the order exists we return a 200 http response to stripe.
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        # If it doesnt exist, let's create it just like if the form were
        # submitted.
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                # But we iterate through the bag in json version from
                # the payment intent.
                for item_id, item_data in json.loads(bag).items():
                    product = Merch.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            # If something goes wrong i'll delete the order if it was created
            # and return a 500 error to stripe. This will cause stripe to
            # automatically try the webhook again later.
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # If the order is created by the webhook handler correctly, return a
        # response indicating that.
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    # Handle payment intent failing.
    # It will be sent each time the user payment fails.
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Payment failed Webhook received: {event["type"]}',
            status=200
        )
