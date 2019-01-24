from mixer.auto import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from stock_maintain.factory import NewsFactory
from stock_maintain.models import News
from stock_setup_info.factory import StructureFactory, StructureTypeFactory


class TestNewsApi(APITestCase):
	def setUp(self):
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.stock = mixer.blend('stock_setup_info.models.Stock', structure=self.structure)
		self.news = mixer.blend('stock_maintain.models.News', news_section=self.structure, stock_id=self.stock)
		NewsFactory.create_batch(10, news_section=self.structure, stock_id=self.stock, is_featured=False)
		NewsFactory.create_batch(10, news_section=self.structure, stock_id=self.stock, is_featured=True)
		self.main_featured_news = News.objects.filter(is_featured=True).latest('id')
		self.main_featured_news.is_main = True

	def test_check_featured_news_count(self):
		"""
		This test ensures that all the industries added in the setup method exists when we make a get request
		"""
		# hit the api endpoint
		response = self.client.get(
			reverse("news-list"),{'is_featured': True}
		)
		featured_news_count = News.objects.filter(is_featured=True).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), featured_news_count)

	def test_view_featured_news(self):
		pass

	def test_view_featured_news_not_existing(self):
		pass

	def test_get_news_by_section(self):
		pass

	def test_get_news_by_section_not_existing(self):
		pass

	def test_create_featured_news(self):
		pass

	def test_create_news(self):
		pass

	def test_create_news_with_images(self):
		pass

	def test_create_news_with_files(self):
		pass