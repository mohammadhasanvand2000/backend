# Generated by Django 4.2.3 on 2023-09-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_alter_apikey_options_apikey_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apikey',
            name='key',
        ),
    ]