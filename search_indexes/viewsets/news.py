from django_elasticsearch_dsl_drf.constants import (
	LOOKUP_FILTER_TERMS,
	LOOKUP_FILTER_RANGE,
	LOOKUP_FILTER_PREFIX,
	LOOKUP_FILTER_WILDCARD,
	LOOKUP_QUERY_IN,
	LOOKUP_QUERY_GT,
	LOOKUP_QUERY_GTE,
	LOOKUP_QUERY_LT,
	LOOKUP_QUERY_LTE,
	LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
	FilteringFilterBackend,
	IdsFilterBackend,
	OrderingFilterBackend,
	DefaultOrderingFilterBackend,
	CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, BaseDocumentViewSet

# Example app models
from search_indexes.documents.news import NewsDocument
import search_indexes.serializers
from search_indexes.serializers.news import NewsDocumentSerializer


class NewsDocumentView(BaseDocumentViewSet):
	"""The NewsDocument view."""

	document = NewsDocument
	serializer_class = NewsDocumentSerializer
	lookup_field = 'id'
	filter_backends = [
		FilteringFilterBackend,
		OrderingFilterBackend,
		DefaultOrderingFilterBackend,
		CompoundSearchFilterBackend,
	]
	# Define search fields
	search_fields = (
		'title',
		'content',
		'stock',
		'sec_code',
		'author'
	)
	# Define filtering fields
	filter_fields = {
		'id': {
			'field': '_id',
			'lookups': [
				LOOKUP_FILTER_RANGE,
				LOOKUP_QUERY_IN,
				LOOKUP_QUERY_GT,
				LOOKUP_QUERY_GTE,
				LOOKUP_QUERY_LT,
				LOOKUP_QUERY_LTE,
			],
		},
		'title': 'title.raw',
		'content': 'content.raw',
		'news_date': 'news_date',
		'entry_date': 'entry_date',
		'stock': 'stock.raw',
		'sec_code': 'sec_code.raw',
		'author': 'author.raw',

	}
	# Define ordering fields
	ordering_fields = {
		'id': 'id',
		'title': 'title.raw',
		'news_date': 'news_date',
		'entry_date': 'entry_date',
		'stock': 'stock.raw',
	}
	# Specify default ordering
	ordering = ('id', 'title',)
