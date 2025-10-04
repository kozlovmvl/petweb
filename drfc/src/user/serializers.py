from rest_framework import serializers

from user.models import User


class UserListSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ("id", "username", "last_name", "first_name")
