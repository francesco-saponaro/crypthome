from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Position
# Install and import "requests" library to get data from the API
import requests

import re


# Home page view
def index(request):
    # Get coins data from Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Set query and category to None initially to not get
    # an error when getting to the index page.
    query = None

    # Check whether request.GET exists
    if request.GET:
        # Check whether the text input (named Q) is in request.GET.
        # If it is i'll set it to a variable called query but in
        # lower case.
        if 'q' in request.GET:
            query = request.GET['q'].lower()
            # If the query is blank send error message and redirect to
            # index url.
            if not query:
                messages.error(request, 'You didn`t enter any search criteria')
                return redirect(reverse('home'))

            # Then iterate through api data and search for a
            # match to the query.
            data = [token for token in data if re.search(query, token['id'])]

            # If there is no match to the query send error message and
            # redirect to index url.
            if not data:
                messages.error(request, 'No Cryptocurrencies match your \
                    criteria')
                return redirect(reverse('home'))

    context = {'api_data': data}

    return render(request, 'home/index.html', context)


# Watchlist page view
def watchlist(request, **kwargs):
    # Get coins data from Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    context = {'api_data': data}

    return render(request, 'home/watchlist.html', context)


# Product page view
def token_page(request, token_id):
    # Get coins data from Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Get detailed coin data for the targeted token from Coingecko API
    coins_url = f'https://api.coingecko.com/api/v3/coins/{token_id}'
    coins_data = requests.get(coins_url).json()

    # Get description value from detailed coin data and split it in two parts
    # for the JS text-hiding function.
    # Replace anchor links with empty string.
    # Unfortunately I had to copy exaxt matched string to replace
    # as the following regex were not working somehow, I have taken
    # this regex from stack overflow but were not working. Even the
    # tutors were not able to find the issue as the regex are valid
    # and were tested with a regex validator.
    # ("<(?:a\b[^>]*>|/a>)", "")
    # First part.
    coins_desc = coins_data["description"]["en"][:950]\
        .replace('<a href="https://www.coingecko.com/en?hashing_algorithm=SHA-256">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/litecoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/peercoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/primecoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/eos">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/tron">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/ethereum-still-king-dapps-cryptokitties-need-1-billion-on-eos">', "")\
        .replace('<a href="https://www.coingecko.com/en?category_id=29&view=market">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum_classic">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/qtum">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/neo">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/icon">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/cardano">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/complete-beginners-guide-to-metamask?locale=en">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/trezor-model-t-wallet-review">', "")\
        .replace('<a href="https://www.coingecko.com/en?category_id=29">', "")\
        .replace('<a href="https://www.coingecko.com/en?hashing_algorithm=Proof+of+Stake&view=market">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/bitcoin">', "")\
        .replace('<a href="https://daedaluswallet.io/">', "")\
        .replace('<a href="https://iohk.io/">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum-classic">', "")\
        .replace('<a href="https://cardanofoundation.org/en/">', "")\
        .replace('<a href="https://iohk.io/team/charles-hoskinson/">', "")\
        .replace('<a href="https://iohk.io/team/jeremy-wood/">', "")\
        .replace('<a href="https://emurgo.io/">', "")\
        .replace('<a href="https://iohk.io/team/charles-hoskinson/">', "")\
        .replace('<a href="https://www.crunchbase.com/organization/ripple-labs">', "")\
        .replace('<a href="/coins/litecoin">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/how-to-use-an-ethereum-wallet">', "")\
        .replace("</a>", "")

    # Second part.
    coins_desc_second = coins_data["description"]["en"][950:]\
        .replace('<a href="https://www.coingecko.com/en?hashing_algorithm=SHA-256">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/litecoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/peercoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/primecoin">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/eos">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/tron">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/ethereum-still-king-dapps-cryptokitties-need-1-billion-on-eos">', "")\
        .replace('<a href="https://www.coingecko.com/en?category_id=29&view=market">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum_classic">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/qtum">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/neo">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/icon">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/cardano">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/complete-beginners-guide-to-metamask?locale=en">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/trezor-model-t-wallet-review">', "")\
        .replace('<a href="https://www.coingecko.com/en?category_id=29">', "")\
        .replace('<a href="https://www.coingecko.com/en?hashing_algorithm=Proof+of+Stake&view=market">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/bitcoin">', "")\
        .replace('<a href="https://daedaluswallet.io/">', "")\
        .replace('<a href="https://iohk.io/">', "")\
        .replace('<a href="https://www.coingecko.com/en/coins/ethereum-classic">', "")\
        .replace('<a href="https://cardanofoundation.org/en/">', "")\
        .replace('<a href="https://iohk.io/team/charles-hoskinson/">', "")\
        .replace('<a href="https://iohk.io/team/jeremy-wood/">', "")\
        .replace('<a href="https://emurgo.io/">', "")\
        .replace('<a href="https://iohk.io/team/charles-hoskinson/">', "")\
        .replace('<a href="https://www.crunchbase.com/organization/ripple-labs">', "")\
        .replace('<a href="/coins/litecoin">', "")\
        .replace('<a href="https://www.coingecko.com/buzz/how-to-use-an-ethereum-wallet">', "")\
        .replace("</a>", "")

    # Get targeted token object from position model
    token = get_object_or_404(Position, pk=token_id)

    context = {
        'api_data': data,
        'db_token': token,
        'coins_api_data': coins_data,
        'coins_api_desc': coins_desc,
        'coins_api_desc_second': coins_desc_second,
        }

    return render(request, 'home/token_page.html', context)


# Buy token view
def buy_token(request, token_id):
    # Get coins data from Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Get targeted token object from position model
    token = get_object_or_404(Position, pk=token_id)

    # Gee this token page url with token id, needed on template for "Back
    # to token page" button conditional.
    url = f"https://8000-bronze-stingray-bewdyfh1.ws-eu13.gitpod.io/token_page/{token.id}/"
    print(url)

    context = {
        'api_data': data,
        'db_token': token,
        'url': url,
        }

    return render(request, 'home/buy_token.html', context)


# Portfolio view
def portfolio(request, **kwargs):
    return render(request, 'home/portfolio.html')
