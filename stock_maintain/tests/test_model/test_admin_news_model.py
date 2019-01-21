from django.contrib.admin import AdminSite
from mixer.auto import mixer

from stock_maintain import admin, models
from stock_setup_info.factory import StructureTypeFactory, StructureFactory


class TestNewsAdmin:

	def setUp(self):
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.stock = mixer.blend('stock_setup_info.models.Stock', structure=self.structure)
		self.news = mixer.blend('stock_maintain.models.News', content='Hello this is the main news',
								news_section=self.structure, stock_id=self.stock)

	def test_news_excerpt(self):
		site = AdminSite()
		news_admin = admin.NewsAdmin(models.News, site)
		result = news_admin.excerpt(self.news)
		assert result == 'Hello', 'Should return first few characters'
