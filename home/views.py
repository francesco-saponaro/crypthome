from django.shortcuts import render, redirect, reverse, \
    HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import BuyToken

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

    context = {
        'api_data': data,
        'dont_show_bag': True,
        }

    return render(request, 'home/index.html', context)


# Home page view
def crypto_query(request):
    # Get coins data from Coingecko API
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

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
            results = [token for token in data if re.search(query, token['id'])]

            # Add all results id in a list in order to be used by websocket.
            results_id = [result['id'] for result in results]

            # If there is no match to the query send error message and
            # redirect to index url.
            if not results:
                messages.error(request, 'No Cryptocurrencies match your \
                    criteria')
                return redirect(reverse('home'))

    context = {
        'results': results,
        'results_id': results_id,
        }

    return render(request, 'home/crypto_query.html', context)


# Product page view
def token_page(request, token_id):
    # Get targeted coin data from Coingecko API
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
        {token_id}&order=market_cap_desc&per_page=100&page=1&sparkline=\
            false'
    token = requests.get(url).json()

    # Get detailed coin data for the targeted token from Coingecko API
    token_detail_url = f'https://api.coingecko.com/api/v3/coins/{token_id}'
    token_detail_data = requests.get(token_detail_url).json()

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
    coins_desc = token_detail_data["description"]["en"][:950]\
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
    coins_desc_second = token_detail_data["description"]["en"][950:]\
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

    context = {
        'api_data': token,
        'api_detailed_data': token_detail_data,
        'coins_api_desc': coins_desc,
        'coins_api_desc_second': coins_desc_second,
        }

    return render(request, 'home/token_page.html', context)


# Buy token page view
def buy_token_page(request, token_id):
    # Get targeted coin data from Coingecko API
    url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
        {token_id}&order=market_cap_desc&per_page=100&page=1&sparkline=\
            false'
    token = requests.get(url).json()

    # Gee this token page url with token id, needed on template for "Back
    # to token page" button conditional.
    url = f"https://8000-bronze-stingray-bewdyfh1.ws-eu13.gitpod.io/token_page/{token[0]['id']}/"

    context = {
        'api_data': token,
        'url': url,
        }

    return render(request, 'home/buy_token_page.html', context)


# Buy token view
@require_POST
def buy_token(request, token_id):
    try:
        # Get targeted coin data from Coingecko API
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
            {token_id}&order=market_cap_desc&per_page=100&page=1&sparkline=\
                false'
        token = requests.get(url).json()
        # Get name to pass in success message.
        token_name = token[0]['name']

        # Get user profile
        profile = UserProfile.objects.get(user=request.user)

        # Get instance of BuyToken model, fill it and save it.
        position = BuyToken()
        position.user_profile = profile
        position.token_symbol = token[0]['symbol']
        position.token_price = token[0]['current_price']
        position.gbp_amount = request.POST.get('gbp-amount')
        position.token_amount = int(request.POST.get('gbp-amount')) / \
            token[0]['current_price']
        position.current_total = token[0]['current_price'] * \
            position.token_amount
        position.save()

        # Send success message and redirect to home page.
        messages.success(request, f'Order successfully processed! \
        You bought {position.token_amount} {token_name} for \
            £{position.gbp_amount}. Check your Portfolio page \
                to track your position.')
        return redirect(reverse('home'))
    except Exception as e:
        messages.error(request, 'Sorry, your purchase cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Portfolio view
@login_required
def portfolio(request, **kwargs):
    return render(request, 'home/portfolio.html')
