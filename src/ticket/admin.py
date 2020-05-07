from django.contrib import admin
from .models import Ticket, ChoiceTypeDb, ChoicePriorityDb, ChoiceStatusDb, Comment

admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(ChoiceTypeDb)
admin.site.register(ChoicePriorityDb)
admin.site.register(ChoiceStatusDb)
