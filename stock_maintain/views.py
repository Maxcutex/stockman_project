import pdb

from django.shortcuts import render
from rest_framework import viewsets, decorators
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

from stockman_project.permissions import IsAdminOrReadOnly
from .serializers import NewsSerializer, NewsImageSerializer, PriceListSerializer, NewsFileSerializer, \
	AnalysisOpinionSerializer, SiteAuthorSerializer
from .models import News, NewsImage, PriceList, NewsFile, AnalysisOpinion, SiteAuthor
import stock_maintain.services as stock_maintain_services
# Create your views here.
from tablib import Dataset


class AnalysisView(viewsets.ModelViewSet):
	queryset = AnalysisOpinion.objects.get_queryset().order_by('-id')
	serializer_class = AnalysisOpinionSerializer
	filter_fields = ('title', 'opinion_date')

	@decorators.action(methods=['get'], detail=False, url_path='view-date-range')
	def view_date_range(self, request, *args, **kwargs):
		analysis_list = stock_maintain_services.list_analysis_range(
			query_params=request.query_params,
		)
		paginate = kwargs.get('paginate')
		if paginate is not None:
			page = self.paginate_queryset(analysis_list)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

		serializer = AnalysisOpinionSerializer(analysis_list, many=True)
		return Response(serializer.data)

	@decorators.action(methods=['get'], detail=False, url_path='list-by-section')
	def list_by_section(self, request, *args, **kwargs):
		analysis_list = stock_maintain_services.list_analysis_by_section(
			query_params=request.query_params,
		)
		paginate = kwargs.get('paginate')
		if paginate is not None:
			page = self.paginate_queryset(analysis_list)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

		serializer = AnalysisOpinionSerializer(analysis_list, many=True)
		return Response(serializer.data)


class SiteAuthorView(viewsets.ModelViewSet):
	queryset = SiteAuthor.objects.get_queryset().order_by('-id')
	serializer_class = SiteAuthorSerializer


class NewsView(viewsets.ModelViewSet):
	queryset = News.objects.get_queryset().order_by('-id')
	serializer_class = NewsSerializer
	filter_fields = ('is_featured', 'stock_id', 'news_date', 'sec_code')

	@decorators.action(methods=['get'], detail=False, url_path='view-date-range')
	def view_date_range(self, request, *args, **kwargs):
		news_list = stock_maintain_services.list_news_range(
			query_params=request.query_params,
		)
		paginate = kwargs.get('paginate')
		if paginate is not None:
			page = self.paginate_queryset(news_list)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

		serializer = NewsSerializer(news_list, many=True)
		return Response(serializer.data)

	@decorators.action(methods=['get'], detail=False, url_path='list-by-section')
	def list_by_section(self, request, *args, **kwargs):
		news_list = stock_maintain_services.list_news_by_section(
			query_params=request.query_params,
		)
		paginate = kwargs.get('paginate')
		if paginate is not None:
			page = self.paginate_queryset(news_list)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

		serializer = NewsSerializer(news_list, many=True)
		return Response(serializer.data)


class NewsImageView(viewsets.ModelViewSet):
	queryset = NewsImage.objects.all()
	serializer_class = NewsImageSerializer


class NewsFileView(viewsets.ModelViewSet):
	queryset = NewsFile.objects.all()
	serializer_class = NewsFileSerializer


class PriceListView(viewsets.ModelViewSet):
	queryset = PriceList.objects.get_queryset().order_by('-id')
	serializer_class = PriceListSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('price_date', 'stock', 'sec_code')
	permission_classes = (IsAdminOrReadOnly,)

	@decorators.action(methods=['get'], detail=False, url_path='view-date-range')
	def view_date_range(self, request, *args, **kwargs):
		price_list = stock_maintain_services.list_price_range(
			query_params=request.query_params,
		)
		paginate = kwargs.get('paginate')
		if paginate is not None:
			page = self.paginate_queryset(price_list)
			if page is not None:
				serializer = self.get_serializer(page, many=True)
				return self.get_paginated_response(serializer.data)

		serializer = PriceListSerializer(price_list, many=True)
		return Response(serializer.data)

# def simple_upload(request):
# 	if request.method == 'POST':
# 		person_resource = PersonResource()
# 		dataset = Dataset()
# 		new_persons = request.FILES['myfile']
#
# 		imported_data = dataset.load(new_persons.read())
# 		result = person_resource.import_data(
# 			dataset, dry_run=True)  # Test the data import
#
# 		if not result.has_errors():
# 			person_resource.import_data(
# 				dataset, dry_run=False)  # Actually import now
#
# 	return render(request, 'core/simple_upload.html')
