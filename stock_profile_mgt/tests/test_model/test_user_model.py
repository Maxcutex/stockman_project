import pdb

from rest_framework.test import APITestCase
from faker import Faker

from stock_profile_mgt.factory import UserProfileFactory
from stock_profile_mgt.models import UserProfile


class BaseViewTest(APITestCase):
    def setUp(self):
        self.user = UserProfileFactory()
        self.user_model = UserProfile.objects.create(
            first_name="Eno", last_name="Bassey", email="test@example.com"
        )

    def test_user_creation(self):
        assert isinstance(self.user, UserProfile)

    def test_user_name(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        username = self.user.email
        # pdb.set_trace()
        full_name_expected = self.user_model.get_full_name()
        short_name_expected = self.user_model.get_short_name()
        full_name_actual = self.user_model.first_name + " " + self.user_model.last_name
        short_name_actual = self.user_model.first_name
        self.assertEqual(username, self.user.email)
        self.assertEqual(full_name_expected, full_name_actual)
        self.assertEqual(short_name_expected, short_name_actual)
        self.assertEqual(first_name, self.user.first_name)
        self.assertEqual(last_name, self.user.last_name)
