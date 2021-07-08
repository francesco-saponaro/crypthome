from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypthomerch, name='crypthomerch'),
]
