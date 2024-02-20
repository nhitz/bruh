from rest_framework import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, FriendshipRequest


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            # Check if a user with the provided email exists
            user = User.objects.get(email=attrs["email"])

            # Check if the password is correct
            if not user.check_password(attrs["password"]):
                raise User.DoesNotExist

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        # If the user exists and the password is correct, call the superclass's validate method
        data = super().validate(attrs)

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "friends_count",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        fields = (
            "id",
            "created_by",
        )
