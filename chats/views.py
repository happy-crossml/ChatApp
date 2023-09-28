from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
from .models import GroupChat
from firebase_admin import db

from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required
# Create your views here.
def index(request):
    user = request.user
    user = User.objects.filter(username=user.username)
    user_groups = GroupChat.objects.filter(users__in=user)


    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users, 'user_groups': user_groups})

@login_required
def chatPage(request, username):
    
    user = request.user
    user = User.objects.filter(username=user.username)
    user_groups = GroupChat.objects.filter(users__in=user)

    user_obj = User.objects.get(username=username)  
    users = User.objects.exclude(username=request.user.username)
    
    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    db_ref = db.reference('/messages')

    query_result = db_ref.order_by_child('thread_name').equal_to(thread_name).get()

    message_objs = []
    for message_id, message_data in query_result.items():
        message_objs.append({
            'sender': message_data['sender'],
            'message': message_data['message'],
        })

    return render(request, 'main_chat.html', context={'user': user_obj, 'users': users, 'messages': message_objs, 'user_groups':user_groups})

@login_required
def create_group(request):
    participants = User.objects.all().exclude(id=request.user.id)
    
    if request.method == 'POST':
        group_name = request.POST['group_name']
        selected_participant_ids = request.POST.getlist('participants')

        new_group = GroupChat.objects.create(group_name=group_name)
        new_group.users.set(selected_participant_ids)
       
        return redirect('/') 
    
    return render(request, 'create_group.html', {'participants': participants})


@login_required
def group_chat(request, group_name):

    current_user = request.user
    user = User.objects.filter(username=current_user.username)
    user_groups =  GroupChat.objects.filter(users__in=user)
    
    selected_group = GroupChat.objects.get(group_name=group_name)
    
    users = User.objects.exclude(username=current_user.username)
    
    message_objs = []
    thread_name = f'group_chat_{selected_group.id}'
    
    if thread_name:
        db_ref = db.reference('/messages')
        query_result = db_ref.order_by_child('thread_name').equal_to(thread_name).get()

        for message_id, message_data in query_result.items():
            message_objs.append({
                'sender': message_data['sender'],
                'message': message_data['message'],
            })

    return render(request, 'group_chat.html', context={
        'current_user': current_user,
        'user_groups': user_groups,
        'selected_group': selected_group,
        'users': users,
        'messages': message_objs,
    })
