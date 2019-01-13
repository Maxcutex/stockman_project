from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from .serializers import NewsSerializer, NewsImageSerializer, PriceListSerializer, NewsFileSerializer
from .models import News, NewsImage, PriceList, NewsFile
# Create your views here.
from tablib import Dataset


class NewsView(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer
	filter_fields = ('is_featured', 'stock_id', 'news_section', 'date', 'sec_code')


class NewsImageView(viewsets.ModelViewSet):
	queryset = NewsImage.objects.all()
	serializer_class = NewsImageSerializer


class NewsFileView(viewsets.ModelViewSet):
	queryset = NewsFile.objects.all()
	serializer_class = NewsFileSerializer


class PriceListView(viewsets.ModelViewSet):
	queryset = PriceList.objects.all()
	serializer_class = PriceListSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('price_date', 'stock_id', 'sec_code')

	@list_route(methods=['get'], url_path='view-by-date')
	def view_by_date(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		queryset = self.filter_queryset(queryset)

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = PriceListSerializer(queryset, many=True, context=self.get_serializer_context())
		return Response(serializer.data)


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
