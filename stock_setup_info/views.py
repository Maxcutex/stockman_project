from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets, permissions, decorators
from rest_framework.permissions import AllowAny

from stockman_project.settings.pagination_defaults import DefaultResultsSetPagination
from .models import (Industry, Structure, StructureType, Stock, StockManagement, MainSector, SubSector, SectionGroup)
from .serializers import (
    IndustrySerializer, StructureSerializer, StructureTypeSerializer,
    StockManagementSerializer, StockSerializer, MainSectorSerializer, SubSectorSerializer, StockMiniSerializer,
    CategorySerializer)

from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
import stock_setup_info.services as stock_setup_info_services

# class IndustryView(viewsets.ModelViewSet):
class IndustryView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = Industry.objects.get_queryset().order_by('-id')
    serializer_class = IndustrySerializer
    authentication_classes = ()
    pagination_class = DefaultResultsSetPagination
    #permission_classes = (AllowAny,)
    #pagination_class = None



class MainSectorView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = MainSector.objects.get_queryset().order_by('-id')
    serializer_class = MainSectorSerializer
    authentication_classes = ()
    pagination_class = DefaultResultsSetPagination


class SubSectorView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = SubSector.objects.get_queryset().order_by('-id')
    serializer_class = SubSectorSerializer
    authentication_classes = ()
    pagination_class = DefaultResultsSetPagination
    

class StructureView(viewsets.ModelViewSet):
    queryset = Structure.objects.get_queryset().order_by('-id')
    serializer_class = StructureSerializer
    pagination_class = DefaultResultsSetPagination


class StructureTypeView(viewsets.ModelViewSet):
    queryset = StructureType.objects.get_queryset().order_by('-id')
    serializer_class = StructureTypeSerializer
    pagination_class = DefaultResultsSetPagination


class CategoryView(viewsets.ModelViewSet):
    queryset = SectionGroup.objects.get_queryset()
    serializer_class = CategorySerializer
    pagination_class = DefaultResultsSetPagination


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.get_queryset().order_by('-id')
    serializer_class = StockSerializer
    pagination_class = DefaultResultsSetPagination

    @decorators.action(methods=['get'], detail=False, url_path='all')
    def all(self, request, *args, **kwargs):
        stocks = Stock.objects.get_queryset().order_by('stock_code')
        serializer = StockMiniSerializer(stocks, many=True)
        return Response(serializer.data)

    @decorators.action(methods=['get'], detail=False, url_path='by-code')
    def by_code(self, request, *args, **kwargs):
        stock = stock_setup_info_services.get_stock_by_code(
            query_params=request.query_params,
        )
        paginate = kwargs.get('paginate')
        if paginate is not None:
            page = self.paginate_queryset(stock)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    @decorators.action(methods=['get'], detail=False, url_path='search-like-name')
    def search_like_name(self, request, *args, **kwargs):
        stocks = stock_setup_info_services.stock_search_like_name(
            query_params=request.query_params,
        )
        paginate = kwargs.get('paginate')
        if paginate is not None:
            page = self.paginate_queryset(stocks)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


class StockManagementView(viewsets.ModelViewSet):
    queryset = StockManagement.objects.get_queryset().order_by('-id')
    serializer_class = StockManagementSerializer
    pagination_class = DefaultResultsSetPagination


class StockApiView(APIView):
    """ Stock View using Api View """
    pagination_class = DefaultResultsSetPagination

    def get(self, request: object, format: object = None) -> object:
        """ Returns a list of stock api view """

        stock_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!!', 'stock_apiview': stock_apiview})
