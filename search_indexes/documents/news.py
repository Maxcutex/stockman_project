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
	"""News Elasticsearch document."""



	class Django:
		"""Meta options."""

		model = News  # The model associate with this DocType
		fields = [
			'id','title','content',
			'news_date', 'entry_date',
			'stock', 'author', 'sec_code',
			'is_featured',
			'has_downloadable',
			'is_main',
		]
		related_models = [Stock, SiteAuthor]
