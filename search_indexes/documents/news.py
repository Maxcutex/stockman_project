from django.conf import settings
from django_elasticsearch_dsl import DocType, Index, fields
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


@INDEX.doc_type
class NewsDocument(DocType):
	"""News Elasticsearch document."""

	id = fields.IntegerField(attr='id')

	title = fields.StringField(
		analyzer=html_strip,
		fields={
			'raw': fields.StringField(analyzer='keyword', fielddata=True),
		}
	)

	content = fields.StringField(
		analyzer=html_strip,
		fields={
			'raw': fields.StringField(analyzer='keyword'),
		}
	)
	news_date = fields.DateField()
	entry_date = fields.DateField()

	stock = fields.StringField(
		attr='stock_indexing',
		analyzer=html_strip,
		fields={
			'raw': fields.StringField(analyzer='keyword'),
		}
	)

	author = fields.StringField(
		attr='author_indexing',
		analyzer=html_strip,
		fields={
			'raw': fields.StringField(analyzer='keyword'),
		}
	)

	sec_code = fields.StringField(
		analyzer=html_strip,
		fields={
			'raw': fields.StringField(analyzer='keyword'),
		}
	)

	is_featured = fields.BooleanField()

	has_downloadable = fields.BooleanField()

	is_main = fields.BooleanField()

	class Meta(object):
		"""Meta options."""

		model = News  # The model associate with this DocType
