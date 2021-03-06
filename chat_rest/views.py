from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied, NotFound
from .models import Message, Chat
from rest_framework import generics, permissions
from .serializers import PrivateChatSerializer, RoomSerializer, MessageSerializer, UserSerializer
from . import custom_permission

class UserCreationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'create_user'


class PrivateChatCreationView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = PrivateChatSerializer
    name = 'create_private_chat'
    permission_classes = permissions.IsAuthenticated, custom_permission.IsOneOfUser

    def post(self, request, *args, **kwargs):
        request.data['private'] = True
        return self.create(request, *args, **kwargs)


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'list_messages'
    permission_classes = permissions.IsAuthenticated,

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        chat_id = self.request.data['chat'] = self.kwargs['chat']
        chat = Chat.objects.get(id=chat_id)
        if chat.private and not Chat.objects.filter(users_in_chat=self.request.user, id=chat_id):
            raise PermissionDenied(detail="Private chat")
        return self.queryset.filter(chat=chat).order_by('-created_time')[:self.kwargs['quantity']]


class MessageFixedListView(MessageListView):
    name = 'list_10_messages'

    def get_queryset(self):
        self.kwargs['quantity'] = 10
        return super(MessageFixedListView, self).get_queryset()


class MessageView(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'get_or_update_message'
    permission_classes = permissions.IsAuthenticated, custom_permission.HasAccessToPrivateChat, \
                         custom_permission.IsCurrentUserOwner

    def put(self, request, *args, **kwargs):
        request.data['edited'] = True
        request.data['chat'] = kwargs['chat']
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        request.data['edited'] = True
        return self.partial_update(request, *args, **kwargs)

    def get_object(self):
        chat_id = self.kwargs['chat']
        chat = Chat.objects.get(id=chat_id)
        message_id = self.kwargs['pk']
        try:
            return Message.objects.get(chat=chat, id=message_id)
        except Message.DoesNotExist:
            raise NotFound("in this chat not found message with this id")


class MessageCreationView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    name = 'create_message'
    permission_classes = permissions.IsAuthenticated, custom_permission.HasAccessToPrivateChat

    def post(self, request, *args, **kwargs):
        request.data['chat'] = kwargs['chat']
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RoomCreationView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = RoomSerializer
    name = 'create_room'

    def post(self, request, *args, **kwargs):
        request.data['start_by_user'] = request.user.id
        return self.create(request, *args, **kwargs)