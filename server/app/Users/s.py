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
