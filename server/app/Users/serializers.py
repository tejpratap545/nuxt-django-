from rest_auth.serializers import JWTSerializer as RestAuthJWTSerializer
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework import serializers
from .models import User


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ('email',)


class JSONWebTokenAuthenticationQS(BaseJSONWebTokenAuthentication):
    def get_jwt_value(self, request):
        return request.QUERY_PARAMS.get('jwt')


class JWTSerializer(RestAuthJWTSerializer):
    """
    Serializer for JWT authentication.
    Just to override rest_auth default UserDetailsSerializer.
    Used during login.
    """
    token = serializers.CharField(read_only=True)
    user = CustomUserDetailsSerializer()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
