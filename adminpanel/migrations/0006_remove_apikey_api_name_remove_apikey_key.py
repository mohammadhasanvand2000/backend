# Generated by Django 4.2.3 on 2023-09-03 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_apikey_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='api_name',
        ),
        migrations.RemoveField(
            model_name='apikey',
            name='key',
        ),
    ]
