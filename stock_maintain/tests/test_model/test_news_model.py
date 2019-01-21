
from mixer.auto import mixer
from rest_framework.test import APITestCase

from stock_maintain.models import News
from stock_setup_info.factory import StockFactory, StructureFactory, StructureTypeFactory
from stock_setup_info.models import Stock


class BaseViewTest(APITestCase):

	def setUp(self):
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.stock = mixer.blend('stock_setup_info.models.Stock', structure=self.structure)
		self.news = mixer.blend('stock_maintain.models.News', content='Hello this is the main news', news_section=self.structure, stock_id= self.stock)


class NewsModelCreatedTest(BaseViewTest):

	def test_news_creation(self):
		self.assertIsInstance(self.stock, Stock)
		self.assertIsInstance(self.news, News)
		assert self.stock.pk >= 1, 'Should create an Stock Instance'
		assert self.news.pk >= 1, 'Should create an News Instance'

	def test_news_name(self):
		expected_stock_name = self.stock.name
		self.assertEqual(expected_stock_name, self.stock.name)

	def test_news_get_excerpt(self):
		result = self.news.get_summary(5)
		assert result == 'Hello', 'Should return first few characters of content'

	def test_news_get_summary(self):
		pass

