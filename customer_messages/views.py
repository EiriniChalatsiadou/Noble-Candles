from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomerMessage

@login_required
def message_list_view(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    
    messages = CustomerMessage.objects.all()

    context = {
        'messages': messages,
    }
    
    return render(request, 'customer_messages/message_list.html', context)

@login_required
def message_details(request, message_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    try:
        message = get_object_or_404(CustomerMessage, pk=message_id)
    except Http404:
        return render(request, '404.html')

    context = {
        'message': message,
    }
    return render(request, 'customer_messages/message_details.html', context)

@login_required
def message_delete_view(request, message_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))
    
    message = get_object_or_404(CustomerMessage, pk=message_id)
    message.delete()
    messages.success(request, 'Message deleted!')

    return redirect(reverse('customer_messages'))
