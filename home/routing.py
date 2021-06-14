from django.urls import path

from .consumers import HomeConsumer

ws_urlpatterns = [
    path('ws/home/', HomeConsumer.as_asgi())
]
