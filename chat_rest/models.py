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


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    edited = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
