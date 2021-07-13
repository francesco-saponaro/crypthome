from decimal import Decimal
from django.conf import settings


# Custom context processor to be on all templates.
def bag_contents(request):

    # Empty list for the bag items to live in.
    bag_items = []
    
    total = 0
    product_count = 0

    # If total is less than free delivery threshold, the delivery cost will be
    # the total multiplied by the standard delivery percentage
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        # To tell user how much is left to get free delivery
        free_delivery_delta = total - settings.FREE_DELIVERY_THRESHOLD
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
