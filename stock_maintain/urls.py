from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter



router = SimpleRouter()

router.register('api/v1/News', views.NewsView, basename='news')
router.register('api/v1/Authors', views.SiteAuthorView, basename='author')
router.register('api/v1/Analysis', views.AnalysisView, basename='analysis')
router.register('api/v1/PriceLists', views.PriceListView, basename='pricelist')
# router.register('api/v1/SectorPriceList', views.PriceListAPIView.as_view(), basename='sector_price_list')
router.register('api/v1/NewsImages', views.NewsImageView, basename='newsimages')
router.register('api/v1/NewsFiles', views.NewsFileView, basename='newsfiles')
router.register('api/v1/Quotes', views.QuotesView, basename='quotes')
router.register('api/v1/InsideBusiness', views.InsideBusinessView, basename='insidebusiness')

urlpatterns = [
    path('', include(router.urls)),

]
