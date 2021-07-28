from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, kwargs={'navbar': 'profile'}, name='profile'),
]
