# urls.py

from django.urls import path
from .views import create_ticket, ticket_list

urlpatterns = [
    path('create', create_ticket, name='create_ticket'),
    path('ticket_list', ticket_list, name='ticket_list'),
]
