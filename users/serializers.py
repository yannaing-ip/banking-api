from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, min_length = 8)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'phone', 'password')

    def create(self, validated_data):
        return User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            name = validated_data.get('name', ''),
            phone = validated_data.get('phone', ''),
            password = validated_data['password'],
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'phone', 'created_at')
