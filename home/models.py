from django.db import models
from profiles.models import UserProfile

import uuid


# Model to store tokens data.
class Position(models.Model):
    name = models.CharField(max_length=200)
    id = models.CharField(default="crypto", max_length=100, primary_key=True)
    symbol = models.CharField(max_length=10)
    image = models.URLField()
    price = models.FloatField(default=0, blank=True)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)
    price_change = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


# Model to buy tokens.
class BuyToken(models.Model):
    # This first field is non editable as it will be automatically
    # generated.
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # It has a related name of "token_bought" so we can access the user orders
    # by calling something like "user.userprofile.token_bought".
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=True, blank=True,
                                     related_name='token_bought')
    # Auto generated date.
    date = models.DateTimeField(auto_now_add=True)
    token_symbol = models.CharField(max_length=10)
    token_price = models.DecimalField(max_digits=20, decimal_places=2,
                                      null=False, default=0)
    gbp_amount = models.DecimalField(max_digits=20, decimal_places=2,
                                     null=False, default=0)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       null=False, default=0)
    current_total = models.DecimalField(max_digits=20, decimal_places=2,
                                        null=False, default=0)

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
