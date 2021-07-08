from django.urls import path

from .consumers import HomeConsumer

# Websocket router.
ws_urlpatterns = [
    # path and handler (view), which in Django channels is called consumer.
    path('ws/home/', HomeConsumer.as_asgi())
]
