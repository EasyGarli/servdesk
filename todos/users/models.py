from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    usernamec = models.CharField(max_length=30, unique=True, default='none')
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    bio = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usernamec', 'firstname', 'lastname']

    objects = UserManager()
    

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return self.email
