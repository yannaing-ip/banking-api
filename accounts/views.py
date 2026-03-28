from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer
from drf_yasg.utils import swagger_auto_schema

class CreateAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body = AccountSerializer)
    def post(self, request):
        if Account.objects.filter(user = request.user).exists():
            return Response({'error': 'You already have an account'}, status = status.HTTP_400_BAD_REQUEST)
        account = Account.objects.create(user = request.user)
        return Response(AccountSerializer(account).data, status = status.HTTP_201_CREATED)

class ListAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        accounts = Account.objects.filter(user = request.user)
        return Response(AccountSerializer(accounts, many = True).data)


class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            account = Account.objects.get(pk = pk, user = request.user)
        except Account.DoesNotExist:
            return Response({'error': 'Account not found'}, status = status.HTTP_404_NOT_FOUND)
        return Response(AccountSerializer(account).data)
    def delete(self, request, pk):
        try:
            account = Account.objects.get(pk = pk, user = request.user)
        except Account.DoesNotExist:
            return Response({'error': 'Account not found'}, status = status.HTTP_404_NOT_FOUND)
        account.is_active = False
        account.save()
        return Response({'message': 'Account deactivated'}, status = status.HTTP_200_OK)
