from django.urls import path, include
from . import views
from rest_framework import routers
from stock_profile_mgt.urls import router as profile_router
from stock_maintain.urls import router as maintain_router

router = routers.DefaultRouter()
router.register('api/v1/industries', views.IndustryView, basename='industry')
router.register('api/v1/structures', views.StructureView)
router.register('api/v1/structuretypes', views.StructureTypeView)
router.register('api/v1/stocks', views.StockView)
router.register('api/v1/stock-management', views.StockManagementView)
router.registry.extend(profile_router.registry)
router.registry.extend(maintain_router.registry)

urlpatterns = [
    path('', include(router.urls))
]
