from django.shortcuts import render
from .models import Merch


# All merch view
def all_merch(request):

    # Get all merch objects to be rendered on the template
    merch = Merch.objects.all()

    context = {
        'merch': merch,
    }

    return render(request, 'merch/all_merch.html', context)
