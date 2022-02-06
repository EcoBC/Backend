import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.auth import login

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        # Do not allow anonymous users to join the chat
        # if self.user.is_anonymous:
        #     self.accept()
        #     self.send(text_data=json.dumps({'type': 'chat_message','message': 'ERROR: Please Login Before You Join'}))
        #     self.close()
        # else:
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add) (
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'type': 'chat_message','message': 'You are connected to the main server!'}))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send) (
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message
        }
        )
        

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({'message': message}))