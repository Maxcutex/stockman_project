import pdb

from mixer.auto import mixer
from rest_framework.test import APITestCase

from stock_setup_info.factory import StockFactory, StructureFactory, StructureTypeFactory
from stock_setup_info.models import Stock


class BaseViewTest(APITestCase):

	def setUp(self):
		# self.stock = StockFactory()
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.stock = mixer.blend('stock_setup_info.models.Stock', structure=self.structure)


class StockModelCreatedTest(BaseViewTest):

	def test_stock_creation(self):
		self.assertIsInstance(self.stock, Stock)
		#pdb.set_trace()
		assert self.stock.pk >= 1, 'Should create an Stock Instance'

	def test_stock_name(self):
		expected_stock_name = self.stock.name
		self.assertEqual(expected_stock_name, self.stock.name)
