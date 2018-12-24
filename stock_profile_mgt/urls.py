from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/profile', views.UserProfileView)
router.register('api/v1/login', views.LoginView, base_name='login')


urlpatterns = [
    path('', include(router.urls))
]
