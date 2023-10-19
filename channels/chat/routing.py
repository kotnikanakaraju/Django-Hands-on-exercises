from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from . import consumers
from chat import consumers

application=ProtocolTypeRouter({
    "websocket":URLRouter([
        path("ws/chat/",consumers.as_asgi()),
    ]),

})