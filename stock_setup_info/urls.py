from django.urls import path, include
from . import views
from rest_framework import routers
from stock_profile_mgt.urls import router as profile_router

router = routers.DefaultRouter()
router.register('api/v1/industries', views.IndustryView)
router.register('api/v1/structures', views.StructureView)
router.register('api/v1/structuretypes', views.StructureTypeView)
router.registry.extend(profile_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
