from django.contrib import admin
from .models import Position, BuyToken


class BuyTokenAdmin(admin.ModelAdmin):
    # These fields will be calculated by our model methods.
    readonly_fields = ('user_profile', 'date', 'token_symbol',
                       'token_price', 'gbp_amount',
                       'token_amount')

    # The list display option is to restrict the columns that show up
    # in the order list to only specified items below.
    list_display = ('user_profile', 'date',
                    'token_symbol', 'gbp_amount',
                    'token_amount')

    # And I'll set them to be ordered in reverse chronological order.
    ordering = ('-date',)


# Register your models here.
admin.site.register(Position)
admin.site.register(BuyToken, BuyTokenAdmin)
