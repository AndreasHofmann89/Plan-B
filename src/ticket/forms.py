from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .widgets import BootstrapDateTimePickerInput
from .models import Ticket, Comment
from django.forms.widgets import SelectDateWidget


class TicketFilterForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', 'type']


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class TicketCreateForm(forms.ModelForm):
    date_expire = forms.DateField(widget=DateInput, required=False)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'type', 'date_expire', 'status', 'priority', 'ticket_follower', 'assigned_user']
        # widgets = {'date_expire': SelectDateWidget}
        # exclude = ['date_expire', 'ticket_follower']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
