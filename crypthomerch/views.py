from django.shortcuts import render


# Home page view.
def crypthomerch(request):

    return render(request, 'crypthomerch/crypthomerch.html')
