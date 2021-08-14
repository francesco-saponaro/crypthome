import json
from channels.generic.websocket import AsyncWebsocketConsumer


# THE CONSUMER PROCESS WAS STUDIED ON THE PYPLANE YOUTUBE CHANNEL
# Instance of AsyncWebsocketConsumer class.
# We are accepting the incoming Websocket connection.
# We want to add the incoming connection to a group of channels.
class HomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Group_add takes two arguments, first the name of the group we are
        # adding and then the channel name which is assigned automatically.
        await self.channel_layer.group_add('home', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('home', self.channel_name)

    # This method handles the message, the event is the message that was
    # sent by the get_crypto_data function.
    # We are sending this message to all clients (front end)
    # in the "home" group.
    async def send_new_data(self, event):
        new_data = event['text']
        await self.send(json.dumps(new_data))
