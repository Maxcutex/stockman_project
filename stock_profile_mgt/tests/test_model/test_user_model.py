from rest_framework.test import APITestCase
from faker import Faker

from stock_profile_mgt.factory import UserProfileFactory
from stock_profile_mgt.models import UserProfile


class BaseViewTest(APITestCase):

    def setUp(self):
        self.user = UserProfileFactory()

    def test_user_creation(self):
        assert isinstance(self.user, UserProfile)

    def test_user_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        username = self.user.email
        self.assertEqual(username, self.user.email)
        self.assertEqual(first_name, self.user.first_name)
        self.assertEqual(last_name, self.user.last_name)