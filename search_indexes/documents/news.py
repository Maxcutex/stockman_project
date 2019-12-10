from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer

from stock_maintain.models import News, SiteAuthor
from stock_setup_info.models import Stock

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class NewsDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'news'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

        stock = fields.ObjectField(properties={
            'stock_code': fields.TextField(),
        })
        author = fields.ObjectField(properties={
            'first_name': fields.TextField(),
            'last_name': fields.TextField(),
        })

    class Django:
        """Meta options."""

        model = News  # The model associate with this DocType
        fields = [
            'id', 'title',
            'news_date', 'entry_date',
            'sec_code',
            'is_featured',
            'has_downloadable',
            'is_main',
        ]
        related_models = [Stock, SiteAuthor]

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(NewsDocument, self).get_queryset().select_related(
            'stock', 'author'
        )

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the News instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        if isinstance(related_instance, Stock):
            return related_instance.news_set.all()

