# -*- coding: utf-8 -*-
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import  get_channel_layer
import json
import paramiko

class webterminal(AsyncWebsocketConsumer):
    ssh = paramiko.SSHClient()

    async def connect(self):
        await self.accept()
        await  self.channel_layer.group_add("chat",self.channel_name)

    async def receive(self,text_data=None,bytes_data=None):
        await self.channel_layer.group_send(
            "chat",
            {
             "type":"chat.message",
              "text":"hello word",
            }
        )

    async def disconnect(self, code):
        await self.channel_layer.group_discard("chat",self.channel_name)
        await  self.close()

    async def chat_message(self,event):
        await  self.send(text_data=event["text"])



