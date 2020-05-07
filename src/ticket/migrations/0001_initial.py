# Generated by Django 3.0.2 on 2020-01-11 18:40

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoicePriorityDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('charID', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceStatusDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('charID', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceTypeDb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('charID', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_expire', models.DateTimeField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('OP', 'Open'), ('IP', 'In Progress'), ('DN', 'Done')], default='OP', max_length=2)),
                ('type', models.CharField(choices=[('IN', 'Incident'), ('BG', 'Bug')], default='IN', max_length=2)),
                ('priority', models.CharField(choices=[('LW', 'Low'), ('N', 'Normal'), ('HI', 'High')], default='N', max_length=2)),
                ('assigned_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ManyToManyField(blank=True, to='ticket.Comment')),
                ('ticket_follower', models.ManyToManyField(blank=True, related_name='ticket_follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
