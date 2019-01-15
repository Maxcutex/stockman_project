from rest_framework.test import APITestCase, APIClient

from stock_setup_info.factories.factory import IndustryFactory
from stock_setup_info.models import Industry, Structure, StructureType, Stock, StockManagement
from stock_setup_info.serializers import IndustrySerializer
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
        self.industry = IndustryFactory()


class AllModelCreatedTest(BaseViewTest):

    def test_model_can_create_list_of_industry(self):
        """
        This test ensures that all the industries added in the setup method exists 
        """
        new_count = Industry.objects.count()
        self.assertNotEqual(0, new_count)
