from django.contrib import admin
from chats.models import  UserProfileModel, ChatNotification, GroupChat
# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(ChatNotification)
admin.site.register(GroupChat)
