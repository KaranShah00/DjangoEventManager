# Generated by Django 3.0.2 on 2020-06-27 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200626_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start',
        ),
    ]