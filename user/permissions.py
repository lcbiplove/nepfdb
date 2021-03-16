from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """Only user who owned themselves or are admin are allowed"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to update detail"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id or request.user.is_staff
