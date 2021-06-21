from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('watchlist/', views.watchlist, kwargs={'navbar': 'watchlist'}, name='watchlist'),
    path('token_page/<token_id>/', views.token_page, name='token_page'),
    path('buy_token/<token_id>/', views.buy_token, name='buy_token'),
]
