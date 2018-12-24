from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Industry, Structure, StructureType
from .serializers import IndustrySerializer, StructureSerializer, StructureTypeSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class IndustryView(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class StructureView(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class StructureTypeView(viewsets.ModelViewSet):
    queryset = StructureType.objects.all()
    serializer_class = StructureTypeSerializer


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
