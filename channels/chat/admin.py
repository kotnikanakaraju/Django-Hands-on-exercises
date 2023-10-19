from django.contrib import admin

from .models import ChatMessage

# Register your models here.
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display=('sender', 'message','timestamp')
    list_filter=('sender','timestamp')
