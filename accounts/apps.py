from django.apps import AppConfig
from django.db.models import AutoField

class AccountsConfig(AppConfig):
    default_auto_field = AutoField
    name = 'accounts'