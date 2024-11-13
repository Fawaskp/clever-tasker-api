from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import MyUserManager

class MyUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    name = models.CharField('fullname', max_length=60)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return self.email