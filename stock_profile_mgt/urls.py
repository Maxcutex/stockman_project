from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("api/v1/profile", views.UserProfileView, basename="user_profile")
# router.register('api/v1/login', views.LoginView, basename='login')


urlpatterns = [path("", include(router.urls))]
