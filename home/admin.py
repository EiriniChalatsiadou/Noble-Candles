from django.contrib import admin
from .models import CustomerMessage

class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('date_received', 'name', 'email', 'subject', 'message')
    ordering = ('date_received',)


# Register your models here.
admin.site.register(CustomerMessage, CustomerMessageAdmin)
