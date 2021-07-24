from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


# Checkout view.
def checkout(request):
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

    template = 'checkout/checkout.html'
    # Create an instance of the order form and pass it into
    # context.
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ip7yhJO3fdzlzXp9syaRd9HKtTjJZsJRWbe4wvg8yQo60nQTi7CXE4kmgCL7mpNHWa5wrRaFpq2wNDS0ELuj6W300jDk73kqU',
        'client_secret': 'Test client secret'
    }

    return render(request, template, context)
