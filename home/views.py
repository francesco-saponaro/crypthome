from django.shortcuts import render, get_object_or_404
from .models import Position
# Install and import "requests" library to get data from the API
import requests


# Home page view
def index(request):
    # Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    context = {'api_data': data}

    return render(request, 'home/index.html', context)


# Watchlist page view
def watchlist(request, **kwargs):
    # Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    context = {'api_data': data}

    return render(request, 'home/watchlist.html', context)


# Product page view
def token_page(request, token_id):
    # Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Get object from position model
    token = get_object_or_404(Position, pk=token_id)

    context = {
        'api_data': data,
        'db_token': token,
        }

    return render(request, 'home/token_page.html', context)


# Buy token view
def buy_token(request, token_id):
    # Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Get object from position model
    token = get_object_or_404(Position, pk=token_id)

    context = {
        'api_data': data,
        'db_token': token,
        }

    return render(request, 'home/buy_token.html', context)
