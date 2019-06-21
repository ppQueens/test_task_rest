from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Chat(models.Model):
    start_by_user = models.ForeignKey(User, related_name='start_by_user', blank=True, null=True,
                                      on_delete=models.DO_NOTHING)
    users_in_chat = models.ManyToManyField(User, related_name='users_in_chat')
    private = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "chat {}".format(self.pk)

    def last_message(self):
        message = self.chat_message.last()
        if message:
            return message.content

    def last_message_time(self):
        message = self.chat_message.last()
        if message:
            return message.created_time


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_message', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    edited = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
