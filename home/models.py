from django.db import models


# Model to store tokens data
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
