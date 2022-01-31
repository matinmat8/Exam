from channels.generic.websocket import WebsocketConsumer


class WsTimerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
