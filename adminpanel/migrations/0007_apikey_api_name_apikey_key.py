# Generated by Django 4.2.3 on 2023-09-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0006_remove_apikey_api_name_remove_apikey_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='api_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
