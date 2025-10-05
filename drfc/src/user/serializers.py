from rest_framework import serializers, validators

from user.models import City, User


class CityReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class UserReadSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ("id", "username", "last_name", "first_name", "cities")

    cities = CityReadSerializer(many=True)


class UserCreateSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "cities")

    username = serializers.CharField(
        validators=[validators.UniqueValidator(queryset=User.objects.all())]
    )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("last_name", "first_name", "cities")
