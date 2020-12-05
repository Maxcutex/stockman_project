from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from stock_setup_info.models import Stock

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(number_of_shards=1, number_of_replicas=1)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@INDEX.doc_type
class StockDocument(Document):
    """Stock Elasticsearch document."""

    class Index:
        # Name of the Elasticsearch index
        name = "stock"
        # See Elasticsearch Indices API reference for available settings
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django(object):
        model = Stock  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch

    id = fields.IntegerField(attr="id")

    stock_code = StringField(
        analyzer=html_strip,
        fields={
            "raw": fields.KeywordField(),
        },
    )

    description = StringField(
        analyzer=html_strip,
        fields={
            "raw": fields.KeywordField(),
        },
    )
    industry = StringField(
        attr="industry_indexing",
        analyzer=html_strip,
        fields={
            "raw": fields.KeywordField(),
        },
    )

    sub_sector = StringField(
        attr="sub_sector_indexing",
        analyzer=html_strip,
        fields={
            "raw": fields.KeywordField(),
        },
    )

    is_active = fields.BooleanField()
    name = StringField()
    exchange_code = StringField()
    asset_class_code = StringField()
    contact = StringField()
    registrar = StringField()
    year_end = StringField()
    logo = StringField()
    shares_in_issue = fields.LongField()
    capitalization = fields.LongField()

    class Meta(object):
        parallel_indexing = True
