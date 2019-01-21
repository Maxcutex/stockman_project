from rest_framework import viewsets, status, filters, mixins
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .models import UserProfile
from .serializers import UserProfileSerializer
import rest_framework

from . import permissions

# Create your views here.


class UserProfileView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    """ Handles CRUD actions for profiles """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email')

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [rest_framework.permissions.IsAdminUser]
        elif self.action == 'create':
            permission_classes = [rest_framework.permissions.AllowAny]
        elif self.action == 'destroy':
            permission_classes = [rest_framework.permissions.IsAdminUser]
        else:
            permission_classes = [rest_framework.permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


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
