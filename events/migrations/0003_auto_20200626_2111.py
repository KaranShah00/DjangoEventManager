# Generated by Django 3.0.2 on 2020-06-26 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date_posted',
            new_name='date_created',
        ),
    ]