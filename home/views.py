from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C%20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    context = {'data': data}

    return render(request, 'home/index.html', context)
