from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Merch, Category


# All merch view
def all_merch(request):

    # Get all merch objects to be rendered on the template.
    merch = Merch.objects.all()
    # Set query and category to None initially to not get
    # an error when getting to the all_merch page.
    query = None
    categories = None

    # Check whether request.GET exists
    if request.GET:
        # Check whether 'category' is in request.GET.
        # If it is i'll set it to a variable called categories and
        # then split into a list at the commas.
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # Then pass that list to the filter method.
            # The double underscore here allows us to drill into
            # the related category model (merch and category are
            # related by a foreign key), specifically we are looking
            # for the name field of the category model
            merch = merch.filter(category__name__in=categories)
            # We also grab the category objects whose name is in the url list,
            # so that we can access their fields in the template in order to
            # display for the user which categories they have selected.
            categories = Category.objects.filter(name__in=categories)

        # Check whether the text input (named Q) is in request.GET.
        # If it is i'll set it to a variable called query.
        if 'q' in request.GET:
            query = request.GET['q']
            # If the query is blank send error message and redirect to
            # all_merch url.
            if not query:
                messages.error(request, 'You didn`t enter any search criteria')
                return redirect(reverse('all_merch'))

            # If it isn't use built-in Q object to return results where
            # the query matches either name or description and not
            # necessarily both at the same time, the "|" is the or
            # statement and "i" is for case insensitive.
            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            # Then pass the queries to the filter method.
            merch = merch.filter(queries)

    context = {
        'merch': merch,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'merch/all_merch.html', context)


def product_detail(request, product_id):

    # Get targeted product.
    product = get_object_or_404(Merch, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'merch/product_detail.html', context)
