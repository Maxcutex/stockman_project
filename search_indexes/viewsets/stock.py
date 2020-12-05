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
    LOOKUP_QUERY_ISNULL,
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
from search_indexes.documents.stock import StockDocument
import search_indexes.serializers
from search_indexes.serializers.stock import StockDocumentSerializer


class StockDocumentView(BaseDocumentViewSet):
    """The StockDocument view."""

    document = StockDocument
    serializer_class = StockDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        "name",
        "stock_code",
        "industry",
        "sub_sector",
    )
    # Define filtering fields
    filter_fields = {
        "id": {
            "field": "_id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
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
                LOOKUP_QUERY_ISNULL,
            ],
        },
        "name": "name",
        # 'stock_code': 'stock_code.raw',
        "stock_code": {
            "field": "stock_code",
            "lookups": [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],
        },
        "stock_code.raw": {
            "field": "stock_code.raw",
            "lookups": [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],
        },
        "industry": "industry.raw",
        "sub_sector": "sub_sector.raw",
    }
    # Define ordering fields
    ordering_fields = {
        "id": "id",
        "name": "name",
        "stock_code": "stock_code.raw",
    }
    # Specify default ordering
    ordering = ("id", "stock_code", "name")
