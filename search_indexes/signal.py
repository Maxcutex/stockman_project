from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
	"""
	Update document on added/changed records.
    """

	app_label = sender._meta.app_label
	model_name = sender._meta.model_name
	instance = kwargs['instance']

	if app_label == 'news':
		# If it is `news.stock` that is being updated.
		if model_name == 'stock':
			instances = instance.news.all()
			for _instance in instances:
				registry.update(_instance)

		# If it is `news.Author` that is being updated.
		if model_name == 'author':
			instances = instance.news.all()
			for _instance in instances:
				registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
	"""
	Update document on deleted records.
    """

	app_label = sender._meta.app_label
	model_name = sender._meta.model_name
	instance = kwargs['instance']

	if app_label == 'news':
		# If it is `news.stock` that is being updated.
		if model_name == 'stock':
			instances = instance.news.all()
			for _instance in instances:
				registry.update(_instance)
				registry.delete(_instance, raise_on_error=False)

		# If it is `books.Author` that is being updated.
		if model_name == 'author':
			instances = instance.news.all()
			for _instance in instances:
				registry.update(_instance)
				registry.delete(_instance, raise_on_error=False)
