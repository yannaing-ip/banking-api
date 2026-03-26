from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from .models import Transaction
from .serializers import TransactionSerializer, TransferSerializer

User = get_user_model()


class TransferView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TransferSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        receiver_email = serializer.validated_data['receiver_email']
        amount = serializer.validated_data['amount']
        note = serializer.validated_data.get('note', '')

        if amount <= 0:
            return Response({'error': 'Amount must be greater than 0'}, status = status.HTTP_400_BAD_REQUEST)

        try:
            receiver_user = User.objects.get(email = receiver_email)
        except User.DoesNotExist:
            return Response({'error': 'Receiver not found'}, status = status.HTTP_404_NOT_FOUND)

        try:
            sender_account = Account.objects.get(user = request.user)
        except Account.DoesNotExist:
            return Response({'error': 'You do not have an account'}, status = status.HTTP_404_NOT_FOUND)

        try:
            receiver_account = Account.objects.get(user = receiver_user)
        except Account.DoesNotExist:
            return Response({'error': 'Receiver does not have an account'}, status = status.HTTP_404_NOT_FOUND)

        if sender_account == receiver_account:
            return Response({'error': 'Cannot transfer to yourself'}, status = status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            sender_account = Account.objects.select_for_update().get(pk = sender_account.pk)
            receiver_account = Account.objects.select_for_update().get(pk = receiver_account.pk)

            if sender_account.balance < amount:
                return Response({'error': 'Insufficient balance'}, status = status.HTTP_400_BAD_REQUEST)

            sender_account.balance -= amount
            receiver_account.balance += amount
            sender_account.save()
            receiver_account.save()

            txn = Transaction.objects.create(
                sender = sender_account,
                receiver = receiver_account,
                amount = amount,
                status = 'completed',
                note = note,
            )

        return Response(TransactionSerializer(txn).data, status = status.HTTP_201_CREATED)


class TransactionListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            account = Account.objects.get(user = request.user)
        except Account.DoesNotExist:
            return Response({'error': 'You do not have an account'}, status = status.HTTP_404_NOT_FOUND)

        transactions = Transaction.objects.filter(
            sender = account
        ) | Transaction.objects.filter(
            receiver = account
        )
        transactions = transactions.order_by('-created_at')
        return Response(TransactionSerializer(transactions, many = True).data)
