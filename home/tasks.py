from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
from .models import Position
from django.forms.models import model_to_dict
import requests

channel_layer = get_channel_layer()


@shared_task
def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    tokens = []

    for token in data:
        # Either get an instance of the Position model or create it
        p, _ = Position.objects.get_or_create(name=token['name'])

        p.symbol = token['symbol']
        p.image = token['image']

        if p.price > token['current_price']:
            direction = 'lower'
        elif p.price == token['current_price']:
            direction = 'same'
        elif p.price < token['current_price']:
            direction = 'higher'

        p.price = token['current_price']
        p.rank = token['market_cap_rank']
        p.market_cap = token['market_cap']
        p.price_change = token['price_change_percentage_24h']
        p.save()

        display = model_to_dict(p)
        display.update({'direction': direction})
        tokens.append(display)

    async_to_sync(channel_layer.group_send)('home', {'type': 'send_new_data',
                                                     'text': tokens})
