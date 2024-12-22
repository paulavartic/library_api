from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Checks if the user is administrator."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class IsOwner(permissions.BasePermission):
    """Checks if the user is owner."""

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
