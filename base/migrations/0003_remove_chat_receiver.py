# Generated by Django 4.0.5 on 2022-07-30 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_chat_delete_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='receiver',
        ),
    ]
