from django.contrib import admin
from .models import Chat


# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    list_display = '__str__', 'private', 'last_message', 'last_message_time'


admin.site.register(Chat, ChatAdmin)
