from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, UserSerializer
from .serializers import RegisterSerializer, UserSerializer, UpdateUserSerializer

class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(request_body = RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    @swagger_auto_schema(request_body = UpdateUserSerializer)
    def put(self, request):
        serializer = UpdateUserSerializer(request.user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(request.user).data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
