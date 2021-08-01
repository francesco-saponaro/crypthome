from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_merch, name='all_merch'),
    # We must specify the product id should be an integer, otherwise
    # navigating to merch/add/ will interpret the string "add" as a
    # product id.
    # This happens because django always uses the first url it finds a
    # matching pattern for.
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]
