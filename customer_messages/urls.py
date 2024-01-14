from django.urls import path
from .views import message_list_view, message_delete_view

urlpatterns = [
    path('', message_list_view, name='customer_messages'),
    path('delete/<int:message_id>/', message_delete_view, name='message-delete'),

]