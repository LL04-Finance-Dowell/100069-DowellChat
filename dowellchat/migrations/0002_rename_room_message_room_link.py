# Generated by Django 4.0.6 on 2022-09-15 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dowellchat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='room_link',
        ),
    ]
