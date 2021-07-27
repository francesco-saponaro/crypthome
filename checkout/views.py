from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from merch.models import Merch
from bag.contexts import bag_contents

import stripe
import json


# We expect the POST method only in this view.
# Before we call the confirmCardPayment method in the stripe
# javascript, we make a post request to this view.
@require_POST
def cache_checkout_data(request):
    try:
        # We give it the client secret from the payment intent, if
        # we split that at the word secret, the first part of it
        # would be the payment intent id.
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Then I'll set up stripe with the secret key so we can modify
        # the payment intent.
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # I can do so by calling the below method, pass it the
        # payment intent id and tell it what we want to modify.
        # In this case we want to add the user placing the orders,
        # if the wanted to save their info and a json dump of their
        # shopping bag.
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Checkout view.
def checkout(request):
    # Get keys from environment.
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Get the bag from the session.
        bag = request.session.get('bag', {})

        # Put the form data into a dictionary.
        # I am doing this manually in order to skip the save info
        # box which doesnt have a field in the order model.
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Then create an instance of the form with the form_data dictionary.
        order_form = OrderForm(form_data)
        # If form is valid save it
        if order_form.is_valid():
            order = order_form.save()
            # Then iterate through bag items to create a line item for each.
            for item_id, item_data in bag.items():
                try:
                    product = Merch.objects.get(id=item_id)
                    # We check if the item has no sizes by checking if
                    # item_data is an integer, since if it is an integer
                    # we know the item has no sizes and  item_data is
                    # just the quantity.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    # If item_data is not an integer we know it's a dictionary,
                    # which means it has sizes, therefore we iterate through
                    # each size (inner dictionary of items_by_size) and create
                    # a line item accordingly.
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                # If the product isn't found I'll add an error message,
                # delete the empty order and return the user to the
                # shopping bag page.
                except product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Check whether the user wanted to save their profile info
            # to the session.
            request.session['save_info'] = 'save_info' in request.POST

            # Redirect user to the success page with the order number as
            # argument.
            return redirect(reverse('checkout_success', args=[order.order_number]))
        # If form isn't valid.
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # If request method equals GET.
    else:
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


# Successful checkout view.
def checkout_success(request, order_number):
    # Check whether the user wantes to save their information.
    save_info = request.session.get('save_info')
    # Get order created in the previous view through the order number.
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Finally delete shopping bag from the session since it'll
    # no longer be needed.
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
