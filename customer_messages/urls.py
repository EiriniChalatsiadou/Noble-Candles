from django.urls import path
from .views import message_list_view, message_delete_view, message_details

urlpatterns = [
    path('', message_list_view, name='customer_messages'),
    path('<int:message_id>/', message_details, name='message_details'),
    path('delete/<int:message_id>/', message_delete_view, name='message_delete'),

]
