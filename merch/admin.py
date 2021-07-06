from django.contrib import admin
from .models import Category, Merch


# Classes to extend built in model admin class
class MerchAdmin(admin.ModelAdmin):
    # list_display will tell admin which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    # The ordering attribute will sort the displayed fields by it's parameter,
    # which in this case is sku.
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    # list_display will tell admin which fields to display
    list_display = (
        'friendly_name',
        'name',
    )


# Register your models here
admin.site.register(Category, CategoryAdmin)
admin.site.register(Merch, MerchAdmin)
