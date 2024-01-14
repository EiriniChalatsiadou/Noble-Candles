from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from .models import CustomerMessage

def message_list_view(request):
    messages = CustomerMessage.objects.all()

    context = {
        'messages': messages,
    }
    
    return render(request, 'customer_messages/message_list.html', context)

def message_details(request, message_id):

    try:
        message = get_object_or_404(CustomerMessage, pk=message_id)
    except Http404:
        return render(request, '404.html')

    context = {
        'message': message,
    }
    return render(request, 'customer_messages/message_details.html', context)

def message_delete_view(request):
    model = CustomerMessage
    template_name = 'customer_messages/message_confirm_delete.html'
    success_url = reverse_lazy('message-list')  # Redirect to the message list after deletion

