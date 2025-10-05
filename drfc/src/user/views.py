from django.db.models import Prefetch
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import City, User
from user.serializers import (
    UserCreateSerializer,
    UserReadSerializer,
    UserUpdateSerializer,
)


class UserView(ModelViewSet):
    queryset = User.objects.all().prefetch_related(
        Prefetch("cities", queryset=City.objects.all().order_by("name"))
    )
    serializer_class = UserReadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username", "last_name", "first_name"]
    ordering_fields = ["username", "last_name", "first_name"]

    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_user = serializer.save()
        return Response(created_user.id, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        user = self.get_object()
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
