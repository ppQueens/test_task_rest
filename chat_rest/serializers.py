from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Chat, Message
from django.utils import timezone


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    chat = serializers.PrimaryKeyRelatedField(queryset=Chat.objects.all())

    class Meta:
        model = Message
        fields = 'chat', 'author', 'content', 'pk', 'edited'

    def update(self, instance, validated_data):
        created_time = instance.created_time
        if (timezone.now() - created_time).total_seconds() / 60 >= 30:
            raise serializers.ValidationError('Editing time is elapsed')
        return super(MessageSerializer, self).update(instance, validated_data)


class PrivateChatSerializer(serializers.HyperlinkedModelSerializer):
    users_in_chat = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = 'private', 'users_in_chat'


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    start_by_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    users_in_chat = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = 'start_by_user', 'users_in_chat'
