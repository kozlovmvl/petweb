from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserListSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["username", "last_name", "first_name"]
    ordering_fields = ["username", "last_name", "first_name"]
