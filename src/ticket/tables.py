import django_tables2 as tables
from django_tables2 import A

from .models import Ticket


class TicketTable(tables.Table):
    pk = tables.LinkColumn('ticket-detail', args=[A('pk')], verbose_name='ID')
    date_posted = tables.Column(verbose_name='Date created')

    class Meta:
        model = Ticket
        fields = ("pk", "title", "date_posted", "author", "status", "type", "priority")
        template_name = 'django_tables2/bootstrap4.html'
        order_by = '-pk'

