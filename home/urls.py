from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('crypto_query/', views.crypto_query, name='crypto_query'),
    path('portfolio/', views.portfolio, kwargs={'navbar': 'portfolio'},
         name='portfolio'),
    path('token_page/<token_id>/', views.token_page, name='token_page'),
    path('buy_token_page/<token_id>/', views.buy_token_page,
         name='buy_token_page'),
    path('buy_token/<token_id>/', views.buy_token,
         name='buy_token'),
    path('sell_token/<position_id>/', views.sell_token,
         name='sell_token'),
    path('add_funds/', views.add_funds, name='add_funds'),
]
