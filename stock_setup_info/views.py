from django.shortcuts import render
from rest_framework import viewsets
from .models import Industry
from .serializers import IndustrySerializer


class IndustryView(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
