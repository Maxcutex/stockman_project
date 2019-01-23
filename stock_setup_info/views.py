from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny

from .models import (Industry, Structure, StructureType, Stock, StockManagement)
from .serializers import (
    IndustrySerializer, StructureSerializer, StructureTypeSerializer,
    StockManagementSerializer, StockSerializer)

from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response


# class IndustryView(viewsets.ModelViewSet):
class IndustryView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    authentication_classes = ()
    #permission_classes = (AllowAny,)


class StructureView(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class StructureTypeView(viewsets.ModelViewSet):
    queryset = StructureType.objects.all()
    serializer_class = StructureTypeSerializer


class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockManagementView(viewsets.ModelViewSet):
    queryset = StockManagement.objects.all()
    serializer_class = StockManagementSerializer

class StockApiView(APIView):
    """ Stock View using Api View """

    def get(self, request, format=None):
        """ Returns a list of stock api view """

        stock_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!!', 'stock_apiview': stock_apiview})
