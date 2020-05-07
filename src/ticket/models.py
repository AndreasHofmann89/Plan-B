from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class PriorityChoice(models.TextChoices):
    Low = 'LW', _('Low')
    Normal = 'N', _('Normal')
    High = 'HI', _('High')


class StatusChoice(models.TextChoices):
    Open = 'OP', _('Open')
    In_Progress = 'IP', _('In Progress')
    Done = 'DN', _('Done')


class TypeChoice(models.TextChoices):
    Incident = "IN", _("Incident")
    Bug = "BG", _("Bug")


class ChoicePriorityDb(models.Model):
    title = models.CharField(max_length=100)
    charID = models.CharField(max_length=2)

    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.title


class ChoiceStatusDb(models.Model):
    title = models.CharField(max_length=100)
    charID = models.CharField(max_length=2)

    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.title


class ChoiceTypeDb(models.Model):
    title = models.CharField(max_length=100)
    charID = models.CharField(max_length=2)

    def __str__(self):  # __str__ for Python 3, __unicode__ for Python 2
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_expire = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    status = models.CharField(max_length=2, choices=StatusChoice.choices, default=StatusChoice.Open)
    type = models.CharField(max_length=2, choices=TypeChoice.choices, default=TypeChoice.Incident)
    priority = models.CharField(max_length=2, choices=PriorityChoice.choices, default=PriorityChoice.Normal)
    ticket_follower = models.ManyToManyField(User, related_name='ticket_follower', blank=True)
    assigned_user = models.ForeignKey(User, related_name='assigned_user', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.pk})


# Comment of a Ticket
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('ticket-detail', kwargs={'pk': self.ticket.pk})

    class Meta:
        ordering = ['-date_posted']
