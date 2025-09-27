from typing import Self

from user.models import User


class UserQueryService:
    def __init__(self):
        self._queryset = User.objects.all()

    def __call__(self):
        return self._queryset

    def filter(self, query) -> Self:
        return self
