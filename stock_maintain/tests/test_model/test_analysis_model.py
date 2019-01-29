from mixer.auto import mixer
from rest_framework.test import APITestCase

from stock_maintain.models import News, AnalysisOpinion
from stock_setup_info.factory import StockFactory, StructureFactory, StructureTypeFactory
from stock_setup_info.models import Stock


class BaseViewTest(APITestCase):

	def setUp(self):
		self.analysis = mixer.blend('stock_maintain.models.AnalysisOpinion', content='Hello this is the main analysis')



class AnalysisModelCreatedTest(BaseViewTest):

	def test_analysis_creation(self):
		self.assertIsInstance(self.analysis, AnalysisOpinion)
		assert self.analysis.pk >= 1, 'Should create an Analysis Instance'

	def test_analysis_name(self):
		expected_title = self.analysis.title
		self.assertEqual(expected_title, self.analysis.title)

