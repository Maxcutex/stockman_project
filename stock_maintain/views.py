from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NewsSerializer, NewsImageSerializer
from .models import News, NewsImage
# Create your views here.
from tablib import Dataset

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsImageView(viewsets.ModelViewSet):
    queryset = NewsImage.objects.all()
    serializer_class = NewsImageSerializer


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(
            dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(
                dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')
