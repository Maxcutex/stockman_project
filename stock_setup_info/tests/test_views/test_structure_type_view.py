from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from stock_setup_info.factory import StructureTypeFactory
from stock_setup_info.models import StructureType


# Create your tests here.
from stock_setup_info.serializers import StructureTypeSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        StructureTypeFactory.create_batch(3, child_depth=2)
        self.structure_type = StructureTypeFactory(child_depth=2)


class GetAllViewsTest(BaseViewTest):
    def test_get_all_structure_types(self):
        """
        This test ensures that all the industries added in the setup method exists when we make a get request
        """
        # hit the api endpoint
        response = self.client.get(reverse("structure_types-list"))

        # fetch the data from the db
        expected = StructureType.objects.all()
        StructureTypeSerializer(expected, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.data["count"]), 12)

    def test_get_single_structure_type(self):
        pass
