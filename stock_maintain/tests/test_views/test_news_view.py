import pdb
from datetime import datetime, timedelta

from mixer.auto import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from stock_maintain.factory import NewsFactory, NewsCategorySectionFactory
from stock_maintain.models import News
from stock_setup_info.factory import StructureFactory, StructureTypeFactory


class TestNewsApi(APITestCase):
	def setUp(self):
		self.structure_type = StructureTypeFactory(child_depth=2)
		self.structure = StructureFactory(child_depth=2, structure_type=self.structure_type)
		self.stock = mixer.blend('stock_setup_info.models.Stock', structure=self.structure)
		self.news = mixer.blend('stock_maintain.models.News',  stock=self.stock)
		NewsFactory.create_batch(10,  stock=self.stock, is_featured=False)
		NewsFactory.create_batch(10,  stock=self.stock, is_featured=True)
		self.main_featured_news = News.objects.filter(is_featured=True).latest('id')
		self.main_featured_news.is_main = True
		self.p_date = datetime(year=2014, month=11, day=15, hour=0, minute=0, second=0)


	def test_check_featured_news_count(self):
		"""
		This test ensures that news that are featured
		"""
		# hit the api endpoint
		response = self.client.get(
			reverse("news-list"), {'is_featured': True}
		)
		featured_news_count = News.objects.filter(is_featured=True).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), featured_news_count)

	def test_view_news_not_existing(self):
		"""
		This test ensures that proper error is shown for non existing news
		"""
		# hit the api endpoint

		response = self.client.get(
			reverse("news-detail", args=[203]),
		)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
		message = 'Not found.'
		self.assertEqual(response.data['detail'], message)

	def test_get_news_by_section_with_valid_data(self):
		name_for_section = 'World'
		news_section = StructureFactory(child_depth=2, structure_type=self.structure_type, structure_name=name_for_section)
		news_for_section = mixer.blend('stock_maintain.models.News', stock=self.stock)
		NewsCategorySectionFactory(news=news_for_section, section=news_section)

		response = self.client.get(
			reverse("news-list-by-section"), {'section_list': name_for_section}
		)
		search_array = name_for_section.split(',')
		news_by_section = News.objects.filter(category_news__section__structure_name__in=search_array)
		n_count = news_by_section.count()
		pdb.set_trace()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), n_count)

	def test_get_news_by_section_with_invalid_data(self):
		name_for_section = 'Life'
		name_for_section1 = 'Industry'
		news_section = StructureFactory(child_depth=2, structure_type=self.structure_type, structure_name=name_for_section)
		news_for_section = mixer.blend('stock_maintain.models.News', stock=self.stock)
		NewsCategorySectionFactory(news=news_for_section, section=news_section)

		response = self.client.get(
			reverse("news-list-by-section"), {'section_list': name_for_section1}
		)
		search_array = name_for_section.split(',')
		news_by_section = News.objects.filter(category_news__section__structure_name__in=search_array)
		n_count = news_by_section.count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertNotEqual(len(response.data), n_count)

	def test_get_news_by_section_not_existing(self):
		pass

	def test_create_featured_news(self):
		pass

	def test_create_news(self):
		pass

	def test_create_news_with_images(self):
		pass

	def test_create_news_with_sections(self):
		pass

	def test_create_news_with_files(self):
		pass

	def test_get_news_with_images(self):
		pass

	def test_get_news_with_files(self):
		pass

	def test_get_news_with_sections(self):
		pass

	def test_news_list_by_date(self):
		"""
				This test ensures that all news by date is pulled

		"""

		# hit the api endpoint
		response = self.client.get(
			reverse("news-list"),
			{
				'news_date': self.news.news_date
			}
		)
		news_list = News.objects.filter(news_date=self.news.news_date).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(int(response.data['count']), news_list)

	def test_news_list_by_date_range(self):
		"""
				This test ensures that all news for a  date range is returned
				:return:
				"""
		start_date = self.p_date + timedelta(days=-1)
		end_date = self.p_date + timedelta(days=1)
		response = self.client.get(
			reverse("news-view-date-range"),
			{
				'start_date': start_date.strftime('%Y-%m-%d'),
				'end_date': end_date.strftime('%Y-%m-%d'),
			}
		)
		news_list = News.objects.filter(news_date__gte=start_date, news_date__lte=end_date).count()
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), news_list)

	def test_news_list_by_date_range_with_improper_dates(self):
		"""
				This test ensures that no improper date is sent
				:return:
				"""

		response = self.client.get(
			reverse("news-view-date-range"),
			{
				'start_date': '09-2019-05',
				'end_date': '987-56',
				'stock': self.stock.id,
			}
		)
		self.assertRaises(Exception, response)