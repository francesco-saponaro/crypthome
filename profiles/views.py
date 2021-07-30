from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request, **kwargs):
    # Get profile of current user.
    profile = get_object_or_404(UserProfile, user=request.user)

    # If request method is post, as if profile info is being updated.
    if request.method == "POST":
        # Create a new instance of the form with data coming from post.
        # And tell it the instance we are updating is the profile we
        # just retrieved above.
        form = UserProfileForm(request.POST, instance=profile)
        # Then if the form is valid save it and send a success message.
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure\
                 the form is valid.')
    # Else populate the form with the users current profile info.
    else:
        form = UserProfileForm(instance=profile)
    # Use related name "orders" on the Order model to get the
    # current user's orders.
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    # Get the order by the order number.
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    # I will use the checkout success template since it has already
    # has a nice order confirmation.
    # But i will also add a from profile variable to check if the user
    # got there via the order history view.
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
