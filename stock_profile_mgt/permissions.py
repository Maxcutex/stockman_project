from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allow users to edit their own profile
    """

    def has_object_permission(self, request, view, obj):
        """
        Check user is trying to edit their own profile
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class IsPostOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated
