from rest_framework import permissions


class IsGetOrIsAuthenticated(permissions.BasePermission):

	def has_permission(self, request, view):
		# allow all POST requests
		if request.method == 'GET':
			return True

		return request.user and request.user.is_authenticated


class IsGetOrIsAdmin(permissions.BasePermission):

	def has_permission(self, request, view):
		# allow all POST requests
		if request.method == 'GET':
			return True

		return request.user and request.user.is_admin

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
