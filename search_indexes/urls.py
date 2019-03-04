from django.urls import path, include

from search_indexes.viewsets.news import NewsDocumentView
from . import viewsets
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/search/news', NewsDocumentView, basename='search_news')


urlpatterns = [
    path('', include(router.urls)),
]
