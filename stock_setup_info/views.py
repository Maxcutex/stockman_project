from django.shortcuts import render
from rest_framework import viewsets
from .models import Industry, Structure, StructureType
from .serializers import IndustrySerializer

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
