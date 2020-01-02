#
# search_indexes.py
#

from django.utils import timezone
from haystack import indexes
from .models import News


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr="content")
    news_date = indexes.DateTimeField(model_attr="news_date")
    entry_date = indexes.DateTimeField(model_attr="entry_date")
    sec_code = indexes.CharField(model_attr="sec_code")
    is_featured = indexes.BooleanField(model_attr="is_featured")
    has_downloadable = indexes.BooleanField(model_attr="has_downloadable")
    is_main = indexes.BooleanField(model_attr="is_main")

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            entry_date__lte=timezone.now()
        )