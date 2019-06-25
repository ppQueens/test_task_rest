from rest_framework import permissions
from .models import Chat
import json


class HasAccessToPrivateChat(permissions.BasePermission):
    def has_permission(self, request, view):
        chat_id = view.kwargs['chat']
        chat = Chat.objects.get(id=chat_id)
        if chat.private and not Chat.objects.filter(users_in_chat=request.user, id=chat_id):
            return False
        return True


class IsOneOfUser(permissions.BasePermission):
    def has_permission(self, request, view):
        data = json.loads(request.body)

        if not data.get('users_in_chat'):
            data['users_in_chat'] = [request.user.id]
        return request.user.id in data['users_in_chat']


class IsCurrentUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or obj.author == request.user:
            return True
        return False
