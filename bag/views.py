from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages

from merch.models import Merch


# Shopping bag view
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


# THE 3 FUNCTIONS BELOW WERE TAKEN FROM CODE INSTITUTE'S MINI PROJECT
# Add to bag view
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Import product to be used in messages.
    product = get_object_or_404(Merch, pk=item_id)
    # Get quantity and redirect_url from form.
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # If product_size is in the form I will set it equal
    # to a variable named "size".
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the bag variable if it exists in the session, or create it if
    # it doesnt by initializing it as an empty dictionary.
    bag = request.session.get('bag', {})

    # If a product with sizes is being added.
    if size:
        # If the product is already in the bag.
        if item_id in list(bag.keys()):
            # If the same product with the same size is
            # already in the bag, increment its quantity.
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                # Success message.
                messages.success(request, f'Updated size {size.upper()} \
                    {product.name} quantity to \
                        {bag[item_id]["items_by_size"][size]}')
            # Otherwise add the product with the different selected size.
            else:
                bag[item_id]['items_by_size'][size] = quantity
                # Success message.
                messages.success(request, f'Added size {size.upper()} \
                    {product.name} to your bag')
        # If the product is not in the bag, we add it as a dictionary
        # since we may have multiple items with this id but different sizes.
        # This allows us to have a single item id for each item but still
        # track multiple sizes.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            # Success message.
            messages.success(request, f'Added size {size.upper()} \
                {product.name} to your bag')

    # If a product without sizes is being added
    else:
        # If item is already in the bag, update its quantity,
        # otherwise add the item to the bag.
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            # Success message.
            messages.success(request, f'Updated {product.name} quantity to \
                {bag[item_id]}')
        else:
            bag[item_id] = quantity
            # Success message.
            messages.success(request, f'Added {product.name} to your bag')

    # Finally overwrite the variable in the session with the
    # updated version.
    request.session['bag'] = bag

    return redirect(redirect_url)


# Adjust bag view
def adjust_bag(request, item_id):
    """ Adjust quantity of the specified product to the shopping bag """

    # Import product to be used in messages.
    product = get_object_or_404(Merch, pk=item_id)
    # Get quantity from form.
    quantity = int(request.POST.get('quantity'))
    size = None
    # If product_size is in the form I will set it equal
    # to a variable named "size".
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Get the bag variable if it exists in the session, or create it if
    # it doesnt by initializing it as an empty dictionary.
    bag = request.session.get('bag', {})

    # If a product with sizes is being adjusted.
    if size:
        # If quantity is above 0 update quantity.
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            # Success message.
            messages.success(request, f'Updated size {size.upper()} \
                {product.name} quantity to \
                    {bag[item_id]["items_by_size"][size]}')
        # If quantity is below 0 delete the size of the targeted
        # product from the bag.
        else:
            del bag[item_id]['items_by_size'][size]
            # And if that's the only size they had in the bag, in other words
            # if the items_by_size dictionary is now empty, we remove the
            # entire item id, so we don't end up with empty items_bysize
            # dictionaries hanging around.
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            # Success message.
            messages.success(request, f'Removed {size.upper()} \
                {product.name} from your bag')
    # If a product without sizes is being adjustesd.
    else:
        # If quantity is above 0 update quantity.
        if quantity > 0:
            bag[item_id] = quantity
            # Success message.
            messages.success(request, f'Updated {product.name} quantity to \
                {bag[item_id]}')
        # If quantity is below 0 delete the product from the bag.
        else:
            bag.pop[item_id]
            # Success message.
            messages.success(request, f'Removed {product.name} from your bag')

    # Finally overwrite the variable in the session with the
    # updated version.
    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


# Remove from bag view
def remove_from_bag(request, item_id):
    """ Remove the specified product from the shopping bag """
    try:
        # Import product to be used in messages.
        product = get_object_or_404(Merch, pk=item_id)
        size = None
        # If product_size is in the form I will set it equal
        # to a variable named "size".
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Get the bag variable if it exists in the session, or create it if
        # it doesnt by initializing it as an empty dictionary.
        bag = request.session.get('bag', {})

        # If a product with sizes is being deleted.
        if size:
            # Delete the size from the bag's item_by_size dictionary.
            # And if that's the only size they had in the bag, in other words
            # if the items_by_size dictionary is now empty, we remove the
            # entire item id, so we don't end up with empty items_bysize
            # dictionaries hanging around.
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            # Success message.
            messages.success(request, f'Removed {size.upper()} \
                {product.name} from your bag')
        # If a product with no sizes is being deleted.
        else:
            bag.pop(item_id)
            # Success message.
            messages.success(request, f'Removed {product.name} from your bag')

        # Finally overwrite the variable in the session with the
        # updated version.
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        # Error message.
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
