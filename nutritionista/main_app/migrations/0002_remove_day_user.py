# Generated by Django 3.2.9 on 2021-12-14 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='user',
        ),
    ]
