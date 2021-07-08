from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_merch, name='all_merch'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
