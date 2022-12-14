# Generated by Django 4.0.5 on 2022-07-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='receiver',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='room',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
