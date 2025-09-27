from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from user.models import User
from user.query_services import UserQueryService
from user.serializers import UserListSerializer


class UserListQuerySerializer(serializers.Serializer):
    search = serializers.CharField(requered=False, null=True)
    cities = serializers.ListField(required=False, null=True)


class UserListView(ListAPIView[User]):
    serializer_class = UserListSerializer

    def get_queryset(self) -> QuerySet[User]:
        serializer = UserListQuerySerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        service = UserQueryService()
        return service.filter(query=serializer.validated_data)()
