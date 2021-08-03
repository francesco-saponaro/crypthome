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
    token_amount = models.DecimalField(max_digits=30, decimal_places=4,
                                       null=False, default=0)

    def __str__(self):
        return self.token_symbol + "/gbp"
