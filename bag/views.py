from django.shortcuts import render, redirect


# Shopping bag view
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


# Add to bag view
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
            # Otherwise add the product with the different selected size.
            else:
                bag[item_id]['items_by_size'][size] = quantity
        # If the product is not in the bag, we add it as a dictionary
        # since we may have multiple items with this id but different sizes.
        # This allows us to have a single item id for each item but still
        # track multiple sizes.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    # If a product without sizes is being added
    else:
        # If item is already in the bag, update its quantity,
        # otherwise add the item to the bag.
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # Finally overwrite the variable in the session with the
    # updated version.
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
