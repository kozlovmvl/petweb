from django.contrib import admin

from user.models import City, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    search = ("username", "email", "last_name", "first_name")
    filter_horizontal = ("cities",)
    readonly_fields = ("id",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
