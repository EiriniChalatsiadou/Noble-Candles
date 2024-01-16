from .models import CustomerMessage
from django.forms import ModelForm
from django import forms


class ContactForm(ModelForm):
    """
    Form to handle contact form submission
    """
    class Meta:
        model = CustomerMessage
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'message': forms.Textarea(attrs={'rows': 10, 'cols': 25, 'style': 'width:100%'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initialise the form attributes
        """

        placeholder_texts = {
            'name': 'Enter your name',
            'email': 'Enter your email address',
            'subject': 'Enter your subject',
            'message': 'Enter your message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder_text = f'{placeholder_texts[field]} *'
            else:
                placeholder_text = placeholder_texts[field]
            # Fix: 'placeholder' instead of 'placeholder_text'
            self.fields[field].widget.attrs['placeholder'] = placeholder_text
            self.fields[field].widget.attrs['aria-label'] = placeholder_text
            self.fields[field].label = False
