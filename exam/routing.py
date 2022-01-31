from django.urls import path
from .consumer import *

ws_urlpatterns = {
    path('ws/getting/timer', WsTimerConsumer.as_asgi())
}