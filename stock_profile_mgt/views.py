from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import UserProfile
from .serializers import UserProfileSerializer

from . import permissions

# Create your views here.


class UserProfileView(viewsets.ModelViewSet):
    """ Handles CRUD actions for profiles """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email')


class LoginView(viewsets.ViewSet):
    """
    Checks email and password and returns an auth token.
    """
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """
        User the ObtainAuthToken APIView to validate and create a token
        """
        return ObtainAuthToken().post(request)
