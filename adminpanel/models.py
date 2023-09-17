from django.db import models
from accounts.models import User
import uuid
from rest_framework_api_key.models import AbstractAPIKey


class Article (models.Model):
    created_at      = models.DateTimeField(auto_now_add=True)
    title           = models.CharField(max_length=200)
    content         = models.TextField()


class Ticket(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    subject         = models.CharField(max_length=200)
    message         = models.TextField()
    response        = models.CharField(max_length=1000,null=True, blank=True)
    is_resolved     = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    resolved_at     = models.DateTimeField(null=True, blank=True)



class Visit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
   



class APIKey(models.Model):
    api_name = models.CharField(max_length=255)
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return '{}{}'.format(self.key,self.api_name)