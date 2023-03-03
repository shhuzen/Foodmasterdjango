import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from .wsgi import *  # add this line to top of your code
import os
import django
import orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(orders.routing.websocket_urlpatterns))
        ),
    }
)
