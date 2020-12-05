import pdb

from rest_framework.test import APITestCase

from stock_setup_info.factory import StructureTypeFactory, RecursiveFactory


# Create your tests here.
from stock_setup_info.models import StructureType


class BaseViewTest(APITestCase):
    def setUp(self):
        self.structure_type = StructureTypeFactory(child_depth=2)
        # pdb.set_trace()
        self.test = RecursiveFactory(child_depth=2)


class StructureTypeModelCreatedTest(BaseViewTest):
    def test_structure_creation(self):
        self.assertIsInstance(self.structure_type, StructureType)
        assert self.structure_type.pk > 1, "Should create an structure_type Instance"

    # def test_structure_name(self):
    # print(self.test)
    # expected_structure_type_name = self.structure_type.structure_type_name
    # self.assertEqual(expected_structure_type_name, self.structure_type.structure_type_name)
