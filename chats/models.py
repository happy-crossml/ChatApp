from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileModel(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=100)
    online_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


class GroupChat(models.Model):
    group_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.group_name
    
class ChatNotification(models.Model):
    # chat = models.ForeignKey(to=ChatModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


# def send_message_to_firebase(group_id, sender_id, message):
#     ref = db.reference(f'/chat_groups/{group_id}/messages')
#     new_message_ref = ref.push()
#     new_message_ref.set({
#         'sender_id': sender_id,
#         'message': message,
#         'timestamp': server_timestamp()
#     })
# Import the necessary modules
    # from django.contrib.auth.models import User
    # from your_app.models import GroupChat  # Replace 'your_app' with the name of your Django app

    # # Get the group you are interested in (replace 'group_name' with the actual group name)
    # group = GroupChat.objects.get(group_name='YourGroupName')

    # # Get all users in that group
    # users_in_group = group.users.all()
