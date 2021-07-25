from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


# Checkout view.
def checkout(request):
    # Get keys from environment.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Get the bag from the session.
    bag = request.session.get('bag', {})
    # If bag is empty.
    if not bag:
        messages.error(request, "There`s nothing in your bag at the moment")
        return redirect(reverse('all_merch'))

    # Imported bag_contents dictionary from contexts.py as Stripe
    # needs the grand total from it.
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    # Multiply the total by a 100 and round it to zero decimal places
    # since stripe will require the amount to charge as an integer.
    stripe_total = round(total * 100)
    # Set secret key on stripe.
    stripe.api_key = stripe_secret_key
    # Create payment intent.
    # Stripe creates a payment intent everytime the user gets to
    # the checkout page.
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    template = 'checkout/checkout.html'
    # Create an instance of the order form and pass it into
    # context.
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
