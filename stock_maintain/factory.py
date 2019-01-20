from django.core.files.base import ContentFile
from faker.providers import internet, lorem
import factory

from stock_maintain.models import NewsImage, NewsFile, News
from stock_setup_info.factory import StructureFactory, StockFactory
from stock_setup_info.models import Industry, StockManagement, StructureType, Structure, Stock
from faker import Faker, Factory

from io import StringIO
from PIL import Image
from django.core.files.base import File

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(lorem)


# def get_image_choice():
#     "Return a random line type from available choices."
#     lt_choices = [x[0] for x in choices.LINE_TYPE_CHOICES]
#     return random.choice(lt_choices)
#
# def get_file_choice():
#     "Return a random line type from available choices."
#     lt_choices = [x[0] for x in choices.LINE_TYPE_CHOICES]
#     return random.choice(lt_choices)

def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
	file_obj = StringIO()
	image = Image.new("RGBA", size=size, color=color)
	image.save(file_obj, ext)
	file_obj.seek(0)
	return File(file_obj, name=name)


class NewsFactory(factory.DjangoModelFactory):
	title = faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
	content = faker.paragraphs(nb=3, ext_word_list=None)
	news_section = factory.SubFactory(StructureFactory)
	date = faker.date()
	entry_date = faker.date()
	stock_id = factory.SubFactory(StockFactory)
	is_featured = faker.boolean()
	has_downloadable = faker.boolean()
	is_main = faker.boolean()
	author = faker.name()

	class Meta:
		model = News


class NewsImageFactory(factory.DjangoModelFactory):
	image_choice = ['size930x620', 'size450x330', 'size300x200']
	news_id = factory.SubFactory(NewsFactory)
	is_main = faker.boolean()
	# image_file = models.ImageField(blank=True, upload_to="images/news_image")
	name = faker.text(10)
	image_type = faker.word(ext_word_list=image_choice)

	image_file = factory.LazyAttribute(
		lambda _: ContentFile(
			factory.django.ImageField()._make_data(
				{'width': 1024, 'height': 768}
			), 'example.jpg'
		)
	)

	class Meta:
		model = NewsImage


class NewsFileFactory(factory.DjangoModelFactory):
	doc_choices = ['pdf', 'word', 'excel']
	news_id = factory.SubFactory(NewsFactory)
	is_main = faker.boolean()
	# doc_file = models.FileField(blank=True, upload_to="files/news_docs")
	name = faker.text(10)
	doc_type = faker.word(ext_word_list=doc_choices)

	doc_file = factory.LazyAttribute(
		lambda _: ContentFile(
			factory.django.FileField()._make_data(
				{'width': 1024, 'height': 768}
			), 'example.jpg'
		)
	)

	class Meta:
		model = NewsFile
