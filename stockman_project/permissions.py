from rest_framework import permissions


class IsGetOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'GET':
            return True

        return request.user and request.user.is_authenticated