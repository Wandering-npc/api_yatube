from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAuthor(permissions.BasePermission):
    """Проверка на авторство при изменении контента."""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True