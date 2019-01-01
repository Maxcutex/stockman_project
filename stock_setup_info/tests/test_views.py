# from django.test import TestCase
#from django.urls import reverse
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Industry, Structure, StructureType, Stock, StockManagement
from ..serializers import IndustrySerializer
# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_industry(name="", exchange_code="", sync_flag="", logo=""):
        if name != "" and exchange_code != "":
            Industry.objects.create(
                name=name, exchange_code=exchange_code, sync_flag=sync_flag, logo=logo
            )

    def setUp(self):
        self.create_industry('Agriculture', 'AG', '0', '0')
        self.create_industry('Finance', 'AG', '0', '0')


class GetAllViewsTest(BaseViewTest):

    def test_get_all_industries(self):
        """
        This test ensures that all the industries added in the setup method exists when we make a get request
        """
        # hit the api endpoint
        # response = self.client.get(
        #     reverse("industries"))

        # # fetch the data from the db
        # expected = Industry.objects.all()
        # serialized = IndustrySerializer(expected, many=True)
        # self.assertEqual(response.data, serialized.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
