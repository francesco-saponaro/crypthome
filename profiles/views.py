from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Profile view.
@login_required
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
    orders = profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'dont_show_bag': True,
    }

    return render(request, template, context)


# Profile's order history view.
@login_required
def order_history(request, order_number):
    # Get profile of current user.
    profile = get_object_or_404(UserProfile, user=request.user)
    # Get the order by the order number.
    order = get_object_or_404(Order, order_number=order_number)

    # If the order being accessed belongs to logged in user.
    if order in profile.orders.all():
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
    # Otherwise inform the user they are trying to access another user
    # order, and redirect them to their profile page.
    else:
        messages.error(request, (
            'The order history you tried to access belongs to another\
                user.'
        ))

        return redirect(reverse('profile'))
