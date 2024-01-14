from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import CustomerMessage

def message_list_view(request):
    messages = CustomerMessage.objects.all()

    context = {
        'messages': messages,
    }
    
    return render(request, 'customer_messages/message_list.html', context)

def message_delete_view(request):
    model = CustomerMessage
    template_name = 'customer_messages/message_confirm_delete.html'
    success_url = reverse_lazy('message-list')  # Redirect to the message list after deletion

