from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class Position(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=100)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)
    price_change = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
