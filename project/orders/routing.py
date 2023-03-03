from django.urls import re_path,path

from orders import consumers
from pywebio.platform.django import webio_view



websocket_urlpatterns = [
    re_path(r"check", consumers.CheckConsumer.as_asgi()),
]