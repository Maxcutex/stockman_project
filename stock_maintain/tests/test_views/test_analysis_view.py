import pdb
from datetime import datetime, timedelta

from mixer.auto import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from stock_maintain.factory import NewsFactory, NewsCategorySectionFactory, AnalysisOpinionFactory, \
	AnalysisCategorySectionFactory
from stock_maintain.models import News, AnalysisOpinion
from stock_setup_info.factory import StructureFactory, StructureTypeFactory


class TestAnalysisApi(APITestCase):
	def setUp(self):
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.analysis = mixer.blend('stock_maintain.models.AnalysisOpinion')
		self.p_date = datetime(year=2014, month=11, day=15, hour=0, minute=0, second=0)
		AnalysisOpinionFactory.create_batch(10, opinion_date=self.p_date)


	def test_check_analysis_count(self):
		"""
		This test ensures that news that are featured
		"""
		# hit the api endpoint
		response = self.client.get(
			reverse("analysis-list"),
		)
		featured_news_count = AnalysisOpinion.objects.filter().count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), featured_news_count)

	def test_view_analysis_not_existing(self):
		"""
		This test ensures that proper error is shown for non existing news
		"""
		# hit the api endpoint

		response = self.client.get(
			reverse("analysis-detail", args=[203]),
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		message = 'Not found.'
		self.assertEqual(response.data['detail'], message)

	def test_view_analysis_existing(self):
		"""
		This test ensures that proper error is shown for non existing news
		"""
		name_for_section = 'World'
		analysis_section = StructureFactory(child_depth=2, structure_type=self.structure_type,
											structure_name=name_for_section)
		analysis_for_section = mixer.blend('stock_maintain.models.AnalysisOpinion')
		AnalysisCategorySectionFactory(analysis=analysis_for_section, section=analysis_section)

		response = self.client.get(
			reverse("analysis-detail", args=[analysis_for_section.id]),
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_analysis_by_section_with_valid_data(self):
		name_for_section = 'World'
		analysis_section = StructureFactory(child_depth=2, structure_type=self.structure_type, structure_name=name_for_section)
		analysis_for_section = mixer.blend('stock_maintain.models.AnalysisOpinion')
		AnalysisCategorySectionFactory(analysis=analysis_for_section, section=analysis_section)

		response = self.client.get(
			reverse("analysis-list-by-section"), {'section_list': name_for_section}
		)
		search_array = name_for_section.split(',')
		analysis_by_section = AnalysisOpinion.objects.filter(category_analysis__section__structure_name__in=search_array)
		n_count = analysis_by_section.count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), n_count)





	def test_analysis_list_by_date(self):
		"""
		This test ensures that all analysis by date is pulled

		"""

		# hit the api endpoint
		response = self.client.get(
			reverse("analysis-list"),
			{
				'opinion_date': self.analysis.opinion_date
			}
		)
		analysis_list = AnalysisOpinion.objects.filter(opinion_date=self.analysis.opinion_date).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), analysis_list)

	def test_analysis_list_by_date_range(self):
		"""
		This test ensures that all analysis for a  date range is returned
		:return:
		"""
		start_date = self.p_date + timedelta(days=-1)
		end_date = self.p_date + timedelta(days=1)
		response = self.client.get(
			reverse("analysis-view-date-range"),
			{
				'start_date': start_date.strftime('%Y-%m-%d'),
				'end_date': end_date.strftime('%Y-%m-%d'),
			}
		)
		analysis_list = AnalysisOpinion.objects.filter(opinion_date__gte=start_date, opinion_date__lte=end_date).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), analysis_list)

	def test_analysis_list_by_date_range_with_improper_dates(self):
		"""
		This test ensures that no improper date is sent
		:return:
		"""

		response = self.client.get(
			reverse("analysis-view-date-range"),
			{
				'start_date': '09-2019-05',
				'end_date': '987-56',
			}
		)
		self.assertRaises(Exception, response)