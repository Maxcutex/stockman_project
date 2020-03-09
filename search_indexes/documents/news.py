from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from stock_maintain.models import News

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class NewsDocument(Document):
    """News Elasticsearch document."""

    class Index:
        # Name of the Elasticsearch index
        name = 'news'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = News  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        # fields = [
        #     'id',
        #     'title',
        #     # 'content',
        #     'news_date',
        #     'entry_date',
        #     # 'stock',
        #     # 'author',
        #     # 'sec_code',
        #     'is_featured',
        #     'is_main',
        #     'has_downloadable',
        #
        # ]
    id = fields.IntegerField(attr='id')

    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )

    content = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )
    news_date = fields.DateField()
    entry_date = fields.DateField()

    stock = fields.TextField(
        attr='stock_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )

    author = fields.TextField(
        attr='author_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )

    sec_code = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )

    is_featured = fields.BooleanField()

    has_downloadable = fields.BooleanField()

    is_main = fields.BooleanField()
    #
    # class Meta(object):
    #     """Meta options."""
    #
    #     model = News  # The model associate with this DocType
