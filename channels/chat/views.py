from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ChatMessage


class ChatRoomView(TemplateView):
    template_name='chat/chat_room.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message'] = ChatMessage.objects.all()