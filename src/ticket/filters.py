from .models import Ticket, TypeChoice, ChoiceTypeDb
import django_filters
from django import forms


class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = {
            'title': ['icontains', ],
            'description': ['icontains', ],
            'date_posted': ['year', ],
            'author': ['exact', ],
            'status': ['exact', ],
            'type': ['exact', ],
            'priority': ['exact', ],
            'assigned_user': ['exact', ],
            'date_expire': ['lt', ],
        }
