from django.shortcuts import render, redirect, reverse, \
    HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from .models import BuyToken, Allowance
# Import decimal in order to be able multiply the current_price
# variable if its a decimal.
from decimal import Decimal

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

    # Get this token page url with token id, needed on template for "Back
    # to token page" button conditional.
    url = f"https://crypthome.herokuapp.com/token_page/{token[0]['id']}/"

    # If user is logged in calculate it's allowance and pass it on view.
    if request.user.is_authenticated:
        # Get user profile to be passed into allowance object.
        profile = UserProfile.objects.get(user=request.user)
        # Get or create allowance object by the user profile, we are
        # using get or create, to create a user_allowance field to
        # populate the view, in case the user has not bought anything yet.
        allowance, _ = Allowance.objects.get_or_create(user=profile)
        # Get the allowance field to be passed into view.
        current_allowance = allowance.user_allowance

        context = {
            'api_data': token,
            'url': url,
            'current_allowance': current_allowance,
            }

        return render(request, 'home/buy_token_page.html', context)

    context = {
        'api_data': token,
        'url': url,
        }

    return render(request, 'home/buy_token_page.html', context)


# Buy token view
@require_POST
def buy_token(request, token_id):
    # If user is logged in buy token otherwise send error message
    # and reload page.
    if request.user.is_authenticated:
        try:
            # If GBP amount is not empty or 0 buy token otherwise send
            # error message and reload page.
            if request.POST.get('gbp-amount') != '' and \
               request.POST.get('gbp-amount') != "0":
                # Get targeted coin data from Coingecko API for math
                # calculation.
                url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
                    {token_id}&order=market_cap_desc&per_page=100&page=1&sparkline=\
                        false'
                token = requests.get(url).json()
                # Get name to pass in success message.
                token_name = token[0]['name']

                # Get user profile to be passed in Allowance and
                # BuyToken objects instances.
                profile = UserProfile.objects.get(user=request.user)

                # Either get an instance of the Allowance model saved in
                # database by the user field or create a new one with
                # the user profile parameter as user.
                current_allowance, _ = Allowance.objects.\
                    get_or_create(user=profile)

                # If user allowance isn't less than the input GBP amount
                # fill and save model, deduct the allowance by the
                # GBP amount and send a success message.
                if not current_allowance.user_allowance < int(
                       request.POST.get('gbp-amount')):
                    # Get instance of BuyToken model, fill it and save it.
                    position = BuyToken()
                    position.user_profile = profile
                    position.token_id = token[0]['id']
                    position.token_symbol = token[0]['symbol']
                    position.token_price = token[0]['current_price']
                    position.gbp_amount = request.POST.get('gbp-amount')
                    position.token_amount = int(
                        request.POST.get('gbp-amount')) / \
                        token[0]['current_price']
                    position.save()

                    # Either get an instance of the Allowance model saved in
                    # database by the user field or create a new one with
                    # the user profile parameter as user.
                    # Then deduct allowance field minus the gbp amount spent.
                    # The "_" is a boolean variable which determined
                    # whether the object was created or not.
                    current_allowance.user_allowance -= \
                        int(request.POST.get('gbp-amount'))
                    current_allowance.save()

                    # Send success message and redirect to home page.
                    messages.success(request, f'Order successfully processed! \
                    You bought {position.token_amount} {token_name} for \
                        £{position.gbp_amount}. Check your Portfolio page \
                            to track your position.')
                    return redirect(reverse('portfolio'))
                else:
                    messages.error(request, 'You don`t have enough funds in your \
                        account. Please buy a smaller amount or sell some \
                            of your positions.')
                    return redirect(reverse('buy_token_page', args=[token_id]))
            else:
                messages.error(request, 'The GBP amount cannot be empty or 0')
                return redirect(reverse('buy_token_page', args=[token_id]))
        except Exception as e:
            messages.error(request, 'Sorry, your purchase cannot be \
                processed right now. Please try again later.')
            return HttpResponse(content=e, status=400)
    else:
        messages.error(request, 'You must create a profile to be \
            able to purchase a token')
        return redirect(reverse('buy_token_page', args=[token_id]))


# Delete product view.
@login_required
def sell_token(request, position_id):
    try:
        # Get instance of BuyToken object by its id.
        position = get_object_or_404(BuyToken, pk=position_id)

        # Get targeted coin data from Coingecko API, needed to get
        # current_price.
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
            {position.token_id}&order=market_cap_desc&per_page=100&page=1&sparkline=\
                false'
        token = requests.get(url).json()

        # Get user profile to be passed into allowance object.
        profile = UserProfile.objects.get(user=request.user)
        # Get object by the user profile.
        current_allowance = get_object_or_404(Allowance, user=profile)
        # Increase allowance field by the multiplication of the position
        # object token_amount field times the token api current_price.
        current_allowance.user_allowance += (position.token_amount *
                                             Decimal(token[0]
                                                     ['current_price']))
        current_allowance.save()

        # Finally delete position.
        position.delete()
        messages.success(request, 'Position sold!')
        return redirect(reverse('portfolio'))
    except Exception as e:
        messages.error(request, 'Sorry, there was an issue with your request\
            . Please try again later.')
        return HttpResponse(content=e, status=400)


# Portfolio view
@login_required
def portfolio(request, **kwargs):
    # Get coins data from Coingecko API. Needed to calculate current total.
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=gbp&ids=\
           bitcoin%2C%20ethereum%2C%20cardano%2C%20dogecoin%2C%20polkadot%2C\
           %20ripple&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    # Get user profile to be passed into filter method and allowance
    # object.
    profile = UserProfile.objects.get(user=request.user)
    # Filter positions by current user and order them descending.
    positions = BuyToken.objects.filter(user_profile=profile).order_by('-date')

    # Create a list containing all positions values. In order to then pass
    # them into the portfolio_value variable below.
    total_positions_value = [position.token_amount * Decimal(
        token['current_price']) for position in positions
        for token in data if position.token_id == token['id']]

    # Get or create allowance object by the user profile, we are
    # using get or create to create a user_allowance field to in the variable
    # below, in case the user has not bought anything yet.
    allowance, _ = Allowance.objects.get_or_create(user=profile)
    # Add the user allowance to the sum of all positions values in the list.
    # Then pass the variable in the template.
    portfolio_value = allowance.user_allowance + sum(total_positions_value)

    # Add user allowance to a variable to be passed in the template.
    # Needed to populate cash available section.
    user_allowance = allowance.user_allowance

    # Add positions's tokens gbp amount into a list of dictionaries
    # to populate the dashboard.
    # AmCharts only works with lists of dictionaries.
    tokens_list = []
    tokens_dict = {}
    for token in positions:
        # Store object symbol and gbp_amount fields in a variable.
        token_id = token.token_symbol.upper()
        print(token_id)
        gbp_amount = int(token.gbp_amount)

        # Initialize the dictionary
        # If the token_id variable is not in the dictionary set it
        # with a value of 0 on the first occurrence.
        if token_id not in tokens_dict:
            tokens_dict[token_id] = 0
            print(tokens_dict)
        # And for next iterations append its gbp_amount value.
        tokens_dict[token_id] += gbp_amount
    print(tokens_dict)

    # Convert the dictionary into separate dictionaries and
    # append them to a list as AmCharts requires.
    for token in tokens_dict.keys():
        temp_token_dict = {
            'token': token,
            'gbp_amount': tokens_dict[token]
        }
        tokens_list.append(temp_token_dict)

    # Also add remaining allowance to chart.
    gbp_dict = {
        'token': "GBP",
        'gbp_amount': int(user_allowance)
        }
    tokens_list.append(gbp_dict)

    context = {
        'positions': positions,
        'data': data,
        'user_allowance': user_allowance,
        'portfolio_value': portfolio_value,
        'tokens_list': tokens_list,
        'dont_show_bag': True,
        }

    return render(request, 'home/portfolio.html', context)


# Add funds view
@login_required
def add_funds(request):
    try:
        # Get user profile to be passed into allowance object.
        profile = UserProfile.objects.get(user=request.user)
        # Get object by the user profile.
        current_allowance = get_object_or_404(Allowance, user=profile)
        # Increase allowance field by £10000
        current_allowance.user_allowance += 10000
        current_allowance.save()

        messages.success(request, 'You have added £10,000 to your allowance!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        messages.error(request, 'Sorry, there was an issue with your request\
            . Please try again later.')
        return HttpResponse(content=e, status=400)


# Handle 404 errors.
def handler404(request, exception):
    return render(request, '404.html')


# Handle 500 errors.
def handler500(request):
    return render(request, '500.html')
