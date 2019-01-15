from rest_framework.test import APITestCase

from stock_setup_info.factories.factory import StockFactory
from stock_setup_info.models import Stock


# Create your tests here.


class BaseViewTest(APITestCase):

	def setUp(self):
		self.stock = StockFactory.create()


class StockModelCreatedTest(BaseViewTest):

	def test_stock_creation(self):
		self.assertIsInstance(self.stock, Stock)

	def test_stock_name(self):
		expected_stock_name = self.stock.name
		self.assertEqual(expected_stock_name, self.stock.name)
