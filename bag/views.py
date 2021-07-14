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

    # Get the bag variable if it exists in the session, or create it if
    # it doesnt by initializing it as an empty dictionary.
    bag = request.session.get('bag', {})

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
