from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Checkout view.
def checkout(request):
    # Get the bag from the session.
    bag = request.session.get('bag', {})
    # If bag is empty.
    if not bag:
        messages.error(request, "There`s nothing in your bag at the moment")
        return redirect(reverse('all_merch'))

    template = 'checkout/checkout.html'
    # Create an instance of the order form and pass it into
    # context.
    order_form = OrderForm()
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
