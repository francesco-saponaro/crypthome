import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from merch.models import Merch
from profiles.models import UserProfile


# THE 2 MODELS BELOW WERE TAKEN FROM CODE INSTITUTE'S MINI PROJECT
# Order model.
class Order(models.Model):
    # This first field is non editable as it will be automatically
    # generated.
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # We use SET_NULL if the user profile is deleted since it will allow us
    # to keep an order history in the admin even if the user is deleted.
    # Null and blank true so users without an account can still make
    # purchases.
    # It has a related name of "orders" so we can access the user orders by
    # calling something like "user.userprofile.orders".
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False,
                           blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # This last three fields will be calculated using a model method.
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    # This field will contain the original shopping bag that created the order.
    original_bag = models.TextField(null=False, blank=False, default='')
    # This field will contain the unique stripe payment intent id.
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    # Update grand total each time a line item is added,
    # accounting for delivery cost.
    def update_total(self):
        # Using the sum function across all line_items_total fields
        # for all lineitems on this order.
        # "or 0" is necessary to set the total to 0 instead of none to
        # prevent an error in case we delete all line items by mistake.
        self.order_total = self.lineitems.\
            aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.\
                STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    # Method to generate a random, unique order number using UUID.
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    # Override the original save method to set the order number
    # if it hasnt been set up already.
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Line item model.
class OrderLineItem(models.Model):
    # Foreign key to the order model with a related name in
    # order to access orders.
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    # Foreign key to the merch model so that we can access all fields
    # of the associated product.
    product = models.ForeignKey(Merch, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # Line item is not editable since it will be automatically calculated
    # when the line item is saved.
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    # Override the original save method to set the lineitem total
    # and update the order total.
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
