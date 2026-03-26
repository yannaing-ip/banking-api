from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'sender', 'receiver', 'amount', 'status', 'reference_id', 'note', 'created_at')
        read_only_fields = ('sender', 'receiver', 'status', 'reference_id', 'created_at')


class TransferSerializer(serializers.Serializer):
    receiver_email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits = 12, decimal_places = 2)
    note = serializers.CharField(required = False, allow_blank = True)
