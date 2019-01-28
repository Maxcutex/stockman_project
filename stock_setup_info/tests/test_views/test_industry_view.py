# from django.test import TestCase
# from django.urls import reverse
import pdb

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from stock_setup_info.factory import IndustryFactory
from stock_setup_info.models import Industry


# Create your tests here.
from stock_setup_info.serializers import IndustrySerializer


class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def test_generate_industries():
		for i in range(100):
			IndustryFactory.create()


	@staticmethod
	def create_industry(name="", exchange_code="", sync_flag="", logo=""):
		if name != "" and exchange_code != "":
			Industry.objects.create(
				name=name, exchange_code=exchange_code, sync_flag=sync_flag, logo=logo
			)

	def setUp(self):
		IndustryFactory.create_batch(10)
		#pdb.set_trace()


class GetAllViewsTest(BaseViewTest):

	def test_get_all_industries(self):
		"""
		This test ensures that all the industries added in the setup method exists when we make a get request
		"""
		# hit the api endpoint
		response = self.client.get(
			reverse("industry-list")
		)

		# fetch the data from the db
		expected = Industry.objects.get_queryset().order_by('-id')
		serialized = IndustrySerializer(expected, many=True)
		self.assertEqual(response.data['results'], serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), 10)
