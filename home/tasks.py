from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
from .models import Position
from django.forms.models import model_to_dict

# Install and import "requests" library to get data from the API.
import requests

# Getting the default channel layer defined in setting.py through
# the imported get_channel layer function, which is an asynchronous
# function.
channel_layer = get_channel_layer()

# The shared_task decorator connects this task to celery.
@shared_task
def get_crypto_data():
    # Coingecko API.
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Empty list to store dictionary, which will be sent to front end
    # via the websocket connection.
    tokens = []

    # Insert data into the database.
    for token in data:
        # Either return an instance of the Position model saved in database
        # or create a new one. The "_" is a boolean variable which determined
        # whether the object was created or not.
        p, _ = Position.objects.get_or_create(name=token['name'])

        p.id = token['id']
        p.symbol = token['symbol']
        p.image = token['image']

        # Compare the price in database with current price in data and
        # create a new variable with a value dependent on their price
        # difference.
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

        # After object is saved in database, convert it into a dictionary
        # with the model_to_dict function.
        # Then update the dictionary by adding a new key, value pair
        # containing the the direction variable set above as value.
        display = model_to_dict(p)
        display.update({'direction': direction})
        # Append dictionary to the empty list.
        tokens.append(display)

    # We are calling the asynchronous get_channel_layer function from this
    # synchronous get_crypto_data function thank to the async_to_sync function.
    # We are sending the added "home" group through the group_send method.
    # The method dictionary takes two keys. The first is the type, which is
    # the name of the method in the HomeConsumer class handling this message,
    # the second key is the data being sent to that method text which in this
    # case is the tokens list defined above.
    async_to_sync(channel_layer.group_send)('home', {'type': 'send_new_data',
                                                     'text': tokens})
