from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/News', views.NewsView)
router.register('api/v1/PriceLists', views.PriceListView)
router.register('api/v1/NewsImages', views.NewsImageView)
router.register('api/v1/NewsFiles', views.NewsFileView)


urlpatterns = [
    path('', include(router.urls))
]
