from django.shortcuts import render, redirect
from customer_messages.forms import ContactForm
from django.contrib import messages


# Create your views here.


def index(request):
    """ A view to return the index page """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, 'Successfully sent Contact form message!')
            return redirect('home')
        else:
            messages.error(request,
                           ('Failed to send contact form message. '
                            'Please ensure the form is valid.'))
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {'form': form})
