"""
ASGI config for crypthome project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypthome.settings')
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from home.routing import ws_urlpatterns


# PART THIS VARIABLE SET UP WAS TAKEN FROM THE YOUTUBE "PYPLANE" CHANNEL
# Instance of ProtocolTypeRouter class.
# First Django channels check the type of connection, either HTTP or
# websocket. If it is a websocket connection it'll be passed to the
# AuthMiddlewareStack class, then to the URLRouter class that passes it
# to the consumer defined in the ws_urlpatterns list in routing.py.
application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
