from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from .validators import validate_iranian_phoneNumber
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email,phoneNumber, password=None, **extra_fields):
        if not email:
            raise ValueError("شماره تلفن الزامی است.")

        user = self.model(username=email or phoneNumber , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

   


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    phoneNumber = models.CharField(
        max_length=11,
        validators=[validate_iranian_phoneNumber],
        unique=True,
    )
    
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phoneNumber']
    backend = 'accounts.authentication.UserPhoneBackend'

    def __str__(self):
        return self.name
