from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chat, Message
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = 'pk', 'username', 'password'

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all(), required=True)

    class Meta:
        model = Message
        fields = 'chat', 'author', 'content', 'pk', 'edited'

    def update(self, instance, validated_data):
        created_time = instance.created_time
        if (timezone.now() - created_time).total_seconds() / 60 >= 30:
            raise serializers.ValidationError('Editing time is elapsed')
        return super(MessageSerializer, self).update(instance, validated_data)


class PrivateChatSerializer(serializers.ModelSerializer):
    users_in_chat = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=True)

    class Meta:
        model = Chat
        fields = 'private', 'users_in_chat'


class RoomSerializer(serializers.ModelSerializer):
    start_by_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    users_in_chat = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = 'start_by_user', 'users_in_chat'
