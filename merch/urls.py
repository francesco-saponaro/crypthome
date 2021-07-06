from django.urls import path
from . import views

urlpatterns = [
    path('all_merch/', views.all_merch, name='all_merch'),
]
