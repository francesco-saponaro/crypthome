from celery import shared_task
from .models import Position

from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests


@shared_task
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C%20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    for token in data:
        p, _ = Position.objects.get_or_create(name=token['name'])
        p.image = token['image']
        p.price = token['current_price']
        p.rank = token['market_cap_rank']
        p.market_cap = token['market_cap']
        p.price_change = token['price_change_percentage_24h']
        p.save()


@periodic_task(run_every=(crontab(minute='*/1')))
def get_crypto_current():
    get_crypto_data.delay()
