from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        blank = True,
        related_name = 'custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank = True,
        related_name = 'custom_user_set'
    )
