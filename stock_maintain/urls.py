from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/News', views.NewsView)
router.register('api/v1/PriceList', views.PriceListView)
router.register('api/v1/NewsImage', views.NewsImageView)


urlpatterns = [
    path('', include(router.urls))
]
