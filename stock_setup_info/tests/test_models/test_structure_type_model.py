from rest_framework.test import APITestCase

from stock_setup_info.factories.factory import  StructureTypeFactory
from stock_setup_info.models import Stock


# Create your tests here.


class BaseViewTest(APITestCase):

	def setUp(self):
		self.structure_type = StructureTypeFactory.create()


class StructureTypeModelCreatedTest(BaseViewTest):

	def test_structure_creation(self):
		self.assertIsInstance(self.structure_type, StructureTypeFactory)

	def test_structure_name(self):
		expected_structure_type_name = self.structure_type.structure_type_name
		self.assertEqual(expected_structure_type_name, self.structure_type.structure_type_name)
