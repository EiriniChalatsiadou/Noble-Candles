from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomerMessage


@login_required
def message_list_view(request):
    # Check if the user is a staff member
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    # Retrieve all customer messages
    messages_list = CustomerMessage.objects.all()

    # Prepare context for rendering the template
    context = {
        'messages': messages_list,
    }

    return render(request, 'customer_messages/message_list.html', context)


@login_required
def message_details(request, message_id):
    # Check if the user is a staff member
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    try:
        # Retrieve the customer message with the given ID
        message = get_object_or_404(CustomerMessage, pk=message_id)
    except Http404:
        return render(request, '404.html')

    # Prepare context for rendering the template
    context = {
        'message': message,
    }
    return render(request, 'customer_messages/message_details.html', context)


@login_required
def message_delete_view(request, message_id):
    # Check if the user is a staff member
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only staff can do that.')
        return redirect(reverse('home'))

    # Retrieve the customer message with the given ID or return a 404 response
    message = get_object_or_404(CustomerMessage, pk=message_id)

    # Delete the customer message
    message.delete()

    # Notify the user about the successful deletion
    messages.success(request, 'Message deleted!')

    # Redirect to the list view after deletion
    return redirect(reverse('customer_messages'))
