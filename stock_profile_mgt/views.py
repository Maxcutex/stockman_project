from rest_auth.views import LoginView
from rest_framework import viewsets, status, filters, mixins

# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer
import rest_framework
from rest_framework.decorators import api_view
from . import permissions


# Create your views here.


@api_view()
def complete_view(request):
    return Response("Email account is activated")


@api_view()
def django_rest_auth_null():
    return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        mydata = {"message": "You have successfully logged in", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response


class UserProfileView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """ Handles CRUD actions for profiles """

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    # authentication_classes = (JWTAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name", "last_name", "email")

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [rest_framework.permissions.IsAdminUser]
        elif self.action == "create":
            permission_classes = [rest_framework.permissions.AllowAny]
        elif self.action == "destroy":
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
