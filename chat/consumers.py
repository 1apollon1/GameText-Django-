import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from . import act_constructor
from MagrasBox.settings import BASE_DIR


def write_in(message, path):
    with open(path, 'r') as f:
        lines = f.readlines()
    if len(lines) == 100:
        del lines[0]
    lines.append(f'{message}\n')
    with open(path, 'w') as f:
        f.write(''.join(lines))


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = "chat_%s" % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()


        self.chat_path = f'{BASE_DIR}/chat/chats_data/{self.scope["url_route"]["kwargs"]["room_id"]}.txt'
        self.action_path = f'{BASE_DIR}/chat/actions_data/{self.scope["url_route"]["kwargs"]["room_id"]}.txt'
        with open(self.chat_path) as f:
            current_chat_text = f.read()
        self.send(text_data=json.dumps({"message": f'{current_chat_text}<---->Old messages<---->'}))
        with open(self.action_path) as f:
            current_actions = f.read()
        self.send(text_data=json.dumps({"message": f'!{current_actions}<---->Old actions<---->'}))


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            member = self.scope['user'].membership_set.get(room_id=self.scope["url_route"]["kwargs"]["room_id"])
            author = member.role
            if member.can_write:
                message = text_data_json["message"]
                is_command = False
                # Send message to room group


                if message[0] == '/':
                    message = act_constructor.com_catcher(author, message)
                    is_command=True
                else:
                    message = f'{author}: {message}'
                if message or message[0] == '!':

                    if not is_command:
                        write_in(message, self.chat_path)
                        async_to_sync(self.channel_layer.group_send)(
                            self.room_group_name, {"type": "chat_message", "message": message}
                        )
                    else:
                        write_in(message, self.action_path)
                        async_to_sync(self.channel_layer.group_send)(
                            self.room_group_name, {"type": "chat_message", "message": f'!{message}'}
                        )
            else:
                raise Exception()
        except:
            self.send(text_data=json.dumps({"message": '*You cant write anything*'}))
    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))