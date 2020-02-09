"""stockman_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView
from django.contrib import admin
from django.urls import path, re_path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from stock_profile_mgt.views import CustomLoginView, complete_view, django_rest_auth_null

admin.site.site_header = "Stock Man Administration"
admin.site.site_title = "Stock Man Admin Portal"
admin.site.index_title = "Welcome to Stock Man Portal"

schema_view = get_schema_view(
   openapi.Info(
      title="StockMan API",
      default_version='v1',
      description="API documentation for Stockman",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path('', include('stock_setup_info.urls')),
                  # path('', include('stock_profile_mgt.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),

                  path('accounts/', include('allauth.urls')),
                  path('', include('rest_auth.urls')),
                  path('login/', CustomLoginView, name='account_login'),

                  re_path(r'registration/account-email-verification-sent/', django_rest_auth_null,
                          name='account_email_verification_sent'),
                  path('registration/complete/', complete_view, name='account_confirm_complete'),
                  path('registration/', include('rest_auth.registration.urls')),
                  path('registration/', RegisterView.as_view(), name='account_signup'),
                  re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/', ConfirmEmailView.as_view(),
                          name='account_confirm_email'),
                  path('api-token-auth/', obtain_jwt_token),
                  path('api-token-refresh/', refresh_jwt_token),
                  path('api-token-verify/', verify_jwt_token),

                  # path('rest-auth/registration/', include('rest_auth.registration.urls')),
                  path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
