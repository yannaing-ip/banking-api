from django.db import models
from django.conf import settings
import uuid


class Transaction(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    sender = models.ForeignKey(
        'accounts.Account',
        on_delete = models.PROTECT,
        related_name = 'sent_transactions',
    )
    receiver = models.ForeignKey(
        'accounts.Account',
        on_delete = models.PROTECT,
        related_name = 'received_transactions',
    )
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'pending')
    reference_id = models.UUIDField(default = uuid.uuid4, unique = True, editable = False)
    note = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount} - {self.status}'
