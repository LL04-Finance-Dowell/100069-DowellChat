# Generated by Django 3.2.3 on 2022-07-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_csvupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]