from django.contrib import admin
from .models import Order, OrderLineItem


# Inline admin class.
# This inline item is to to allow us to add and edit
# line items in the admin right from inside the order model.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # This to add the inlines option above here in
    # the order admin class.
    inlines = (OrderLineItemAdminInline,)

    # These fields will be calculated by our model methods.
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    # This is to specify the order of the Order model fields
    # in the admin interface.
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag',
              'stripe_pid')

    # The list display option is to restrict the columns that show up
    # in the order list to only specified items below.
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # And I'll set them to be ordered in reverse chronological order.
    ordering = ('-date',)


# No need to registrer the OrderLineItem model since
# it's accessible via the inline on the Order model.
admin.site.register(Order, OrderAdmin)
