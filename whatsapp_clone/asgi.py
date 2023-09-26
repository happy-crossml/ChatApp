import os
from django.core.asgi import get_asgi_application
from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chats.consumers import PersonalChatConsumer, OnlineStatusConsumer, NotificationConsumer, GroupChatConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whatsapp_clone.settings')
application = get_asgi_application                                                                                                                                                                                             

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([

            re_path(r'ws/group/(?P<group_id>\d+)/', GroupChatConsumer.as_asgi()),
            re_path(r'ws/personal/(?P<id>\d+)/', PersonalChatConsumer.as_asgi()), 

            # path('ws/group/<int:group_id>/', GroupChatConsumer.as_asgi()),
            # path('ws/personal/<int:id>/', PersonalChatConsumer.as_asgi()),
            path('ws/online/', OnlineStatusConsumer.as_asgi()),
            path('ws/notify/', NotificationConsumer.as_asgi()),
        ])
    )
})
    

   