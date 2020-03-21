from django.urls import path, include

from search_indexes.viewsets.news import NewsDocumentView
from . import viewsets
from rest_framework.routers import SimpleRouter

from .viewsets.stock import StockDocumentView

router = SimpleRouter()

router.register('api/v1/search/news', NewsDocumentView, basename='search_news')
router.register('api/v1/search/stock', StockDocumentView, basename='search_stock')



urlpatterns = [
    path('', include(router.urls)),
]
