import json

from rest_framework import serializers


class NewsDocumentSerializer(serializers.Serializer):
	"""Serializer for the Book document."""

	id = serializers.IntegerField()

	title = serializers.CharField(read_only=True)
	content = serializers.CharField(read_only=True)

	news_date = serializers.DateField(read_only=True)
	entry_date = serializers.DateField(read_only=True)
	stock = serializers.CharField(read_only=True)
	sec_code = serializers.CharField(read_only=True)
	author = serializers.CharField(read_only=True)
	is_featured = serializers.BooleanField(read_only=True)
	has_downloadable = serializers.BooleanField(read_only=True)
	is_main = serializers.BooleanField(read_only=True)

	class Meta(object):
		"""Meta options."""

		fields = (
			'id',
			'title',
			'content',
			'news_date',
			'entry_date',
			'stock',
			'sec_code',
			'author',
			'is_featured',
			'has_downloadable',
			'is_main',
		)
		read_only_fields = fields
