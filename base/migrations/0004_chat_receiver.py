# Generated by Django 4.0.5 on 2022-07-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_chat_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='receiver',
            field=models.TextField(null=True),
        ),
    ]