from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync

# Импорт для асинхронного программирования
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json


class CheckConsumer(WebsocketConsumer):
    name = "Test"
    def connect(self):
        user = self.scope["user"]
        if user.is_authenticated:
            async_to_sync(self.channel_layer.group_add)(
                self.name,self.channel_name
            )
            return self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.name, self.channel_name
        )

    def receive(self,text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.name,{"type":text_data,"status":"Update"}
        )

    def Update(self,event):
        status = event["status"]
        self.send(text_data=status)



