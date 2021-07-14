from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merch.models import Merch


# Custom context processor to be on all templates.
def bag_contents(request):

    # Empty list for the bag items to live in.
    bag_items = []
    total = 0
    product_count = 0
    # Get the bag variable if it exists in the session, or create it if
    # it doesnt by initializing it as an empty dictionary.
    bag = request.session.get('bag', {})

    # For each item in the bag dictionary, I'll first get the product
    # by it's id, then add it's quantity times the price to the total,
    # then increment the product count by the quantity.
    for item_id, quantity in bag.items():
        product = get_object_or_404(Merch, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        # Finally I will add a dictionary containing the product id, the
        # quantity and the actual product object, to the bag_items list.
        # So we can display them anywhere in the site.
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # If total is less than free delivery threshold, the delivery cost will be
    # the total multiplied by the standard delivery percentage
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # To tell user how much is left to get free delivery
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
       'bag_items': bag_items,
       'total': total,
       'product_count': product_count,
       'delivery': delivery,
       'free_delivery_delta': free_delivery_delta,
       'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
       'grand_total': grand_total,
    }

    return context
