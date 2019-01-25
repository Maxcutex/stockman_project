from django.core.files.base import ContentFile
from faker.providers import internet, lorem, python, company
import factory

from stock_maintain.models import NewsImage, NewsFile, News, PriceList, Quote, AsiIndex, BonusTracker, DailyMarketIndex, \
	Dividend, OfferIpo
from stock_setup_info.factory import StructureFactory, StockFactory
from stock_setup_info.models import Industry, StockManagement, StructureType, Structure, Stock
from faker import Faker, Factory

from io import StringIO
from PIL import Image
from django.core.files.base import File

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(lorem)
faker.add_provider(python)
faker.add_provider(company)


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


class PriceListFactory(factory.DjangoModelFactory):
	sign = ['-', '+']
	sec_code = faker.text(10)
	price_date = faker.date()
	price_close = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	x_open = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	x_high = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	x_low = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	x_change = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	offer_bid_sign = faker.word(ext_word_list=sign)
	num_of_deals = faker.random_number()
	volume = faker.random_number()
	x_value = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	dps = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	eps = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	pe = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	rpt = faker.text(10)
	e_time = faker.date()
	e_date = faker.date()
	source = faker.text(10)
	sync_flag = faker.random_number()
	stock = factory.SubFactory(StockFactory)

	class Meta:
		model = PriceList


class QuoteFactory(factory.DjangoModelFactory):
	stock_id = factory.SubFactory(StockFactory)
	sec_code = faker.text(10)
	description = faker.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
	contact = faker.text(10)
	fax = faker.text(10)
	phone = faker.text(10)

	class Meta:
		model = Quote


class AsiIndexFactory(factory.DjangoModelFactory):
	date = faker.date()
	price_close = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price_open = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price_high = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price_low = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price_close = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	price_current = faker.pydecimal(left_digits=None, right_digits=2, positive=True)

	class Meta:
		model = AsiIndex


class BonusTrackerFactory(factory.DjangoModelFactory):
	stock_id = factory.SubFactory(StockFactory)
	sec_code = faker.text(10)
	bonus_val = faker.pyint()
	bonus_aggregate = faker.pyint()
	date_declared = faker.date()

	class Meta:
		model = BonusTracker


class DailyMarketIndexFactory(factory.DjangoModelFactory):
	date = faker.date()
	index = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	deals = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	volume = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	value = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	capital = faker.pydecimal(left_digits=None, right_digits=2, positive=True)

	class Meta:
		model = DailyMarketIndex


class DividendFactory(factory.DjangoModelFactory):
	q_type = ['first_quarter', 'second_quarter', 'third_quarter', 'fourth_quarter']
	stock_id = factory.SubFactory(StockFactory)
	sec_code = faker.text(10)
	quarter_type = faker.word(ext_word_list=q_type)
	interim = faker.pydecimal(left_digits=None, right_digits=2, positive=True)
	bonus = faker.pydecimal(left_digits=None, right_digits=2, positive=True)

	class Meta:
		model = Dividend


class OfferIpoFactory(factory.DjangoModelFactory):
	of_type = [
		'Hybrid Initial Public Offer', 'Hybrid Public Offer', 'Initial Public Offering',
		'Public Offer', 'Rights Issue'
	]
	of_method = ['Offer For Sale', 'Offer For Subscription', 'Rights Issue']
	company_name = faker.company()
	country_id = factory.SubFactory(StructureFactory)
	exchange_code = faker.text(10)
	offer_type = faker.sentences(nb=1, ext_word_list=of_type)
	quarter_type = faker.sentences(nb=1, ext_word_list=of_method)
	open_date = faker.date()
	close_date = faker.date()
	extended_date = faker.date()
	proposed_listing_date = faker.date()
	actual_listing_date = faker.date()

	class Meta:
		model = OfferIpo
