from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', max_length=255,unique=True)
    phone = models.IntegerField(null=True)
    REQUIRED_FIELDS = ['username','phone','first_name','last_name']
    USERNAME_FIELD = 'email'
    class Meta:
        db_table = 'auth_user'

    def get_username(self):
        return str(self.username)