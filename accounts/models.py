from django.db import models
from django.conf import settings
import random


class Account(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'accounts'
    )
    account_number = models.CharField(max_length = 20, unique = True, editable = False)
    balance = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.user.email}'
