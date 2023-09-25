
from django.contrib import admin
from django.urls import path, include
from chats.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('', index, name='home'),
    path('chat/<str:username>/', chatPage, name='chat'),

    path('create_group/',create_group, name='create_group'),
    path('group_chat/<str:group_name>/',group_chat, name='group_chat'),

]
