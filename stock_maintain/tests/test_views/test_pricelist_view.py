import pdb
from datetime import datetime, timedelta

from mixer.auto import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from stock_maintain.factory import PriceListFactory
from stock_maintain.models import  PriceList
from stock_setup_info.factory import StructureFactory, StructureTypeFactory, StockFactory, MainSectorFactory, \
	SubSectorFactory


class TestPriceListApi(APITestCase):
	def setUp(self):
		self.main_sector = MainSectorFactory()
		self.sub_sector = SubSectorFactory(main_sector=self.main_sector)
		self.stock = mixer.blend('stock_setup_info.models.Stock', sub_sector=self.sub_sector)
		self.p_date1 = datetime(year=2014, month=11, day=15, hour=0, minute=0, second=0)
		self.price_list = mixer.blend('stock_maintain.models.PriceList', stock=self.stock, price_date=self.p_date1)
		self.p_date = datetime(year=2014, month=11, day=15, hour=0, minute=0, second=0)
		PriceListFactory.create_batch(20,  stock=self.stock, price_date=self.p_date, sec_code=self.stock.stock_code)

	def test_get_price_list_by_date(self):
		"""
		This test ensures that all price by date
		"""


		# hit the api endpoint
		response = self.client.get(
			reverse("pricelist-list"),
			{
				'price_date': self.price_list.price_date
			}
		)
		price_list = PriceList.objects.filter(price_date=self.price_list.price_date).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), price_list)

	def test_get_price_list_by_range(self):
		"""
		This test ensures that all price for a stock and date range is returned
		:return:
		"""
		start_date = self.p_date + timedelta(days=-1)
		end_date = self.p_date + timedelta(days=1)
		response = self.client.get(
			reverse("pricelist-view-date-range"),
			{
				'start_date': start_date.strftime('%Y-%m-%d'),
				'end_date': end_date.strftime('%Y-%m-%d'),
				'stock': self.stock.id,
			}
		)
		price_list = PriceList.objects.filter(price_date__gte=start_date, price_date__lte=end_date, stock=self.stock.id).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), price_list)

	def test_get_price_list_by_range_with_improper_dates(self):
		"""
		This test ensures that no improper date is sent
		:return:
		"""


		response = self.client.get(
			reverse("pricelist-view-date-range"),
			{
				'start_date': '09-2019-05',
				'end_date': '987-56',
				'stock': self.stock.id,
			}
		)
		self.assertRaises(Exception, response)



