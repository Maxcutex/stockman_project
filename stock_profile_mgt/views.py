from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
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
