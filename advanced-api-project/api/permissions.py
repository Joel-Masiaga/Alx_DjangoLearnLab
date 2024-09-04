from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit or delete an object.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
