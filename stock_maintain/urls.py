from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/News', views.NewsView, basename='news')
router.register('api/v1/PriceLists', views.PriceListView, basename='pricelist')
router.register('api/v1/NewsImages', views.NewsImageView, basename='newsimages')
router.register('api/v1/NewsFiles', views.NewsFileView, basename='newsfiles')


urlpatterns = [
    path('', include(router.urls))
]
