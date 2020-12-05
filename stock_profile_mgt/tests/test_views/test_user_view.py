from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from allauth.account.models import (
    EmailAddress,
)


# from api.s3_services import MockStore
from allauth.utils import get_user_model
from stock_profile_mgt import factory as user_factory

# mockstore = MockStore()


class TestUsersValid(APITestCase):
    def setUp(self):
        self.invalid_token = "Bearer Eyhbfhebjwkfbhjbuw3hiuhufhnffjjfjk"
        self.uploader = user_factory._create_user(self, email="testadmin@gmail.com")

    def _create_login_user_with_verified_email(
        self, email="user@example.com", password="$testeR1234", user_status=False
    ):
        """Tests login """
        user = get_user_model().objects.create(email=email, password=password)
        user.set_password(password)
        user.is_staff = user_status
        user.save()
        EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)
        response = self.client.post(
            reverse("account_login"), {"email": email, "password": password}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["user"]["email"], email)
        return response

    def _signup(self):
        data = {
            "email": "tester@ya.com",
            "password1": "testerA123#",
            "password2": "testerA123#",
            "first_name": "test",
            "last_name": "user",
        }
        response = self.client.post(
            reverse(
                "account_signup",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 201)
        message = "Verification e-mail sent."
        self.assertEqual(response.data["detail"], message)

    def test_user_registration(self):
        data = {
            "email": "tester@ya.com",
            "password1": "testerA123#",
            "password2": "testerA123#",
            "first_name": "test",
            "last_name": "user",
        }
        response = self.client.post(
            reverse(
                "account_signup",
            ),
            data=data,
        )

        self.assertEqual(response.status_code, 201)
        message = "Verification e-mail sent."
        self.assertEqual(response.data["detail"], message)

    def test_login_user_with_verified_email(self):
        """Tests login """

        user = get_user_model().objects.create(
            email="user@example.com", password="testerA1234#"
        )
        user.set_password("testerA1234#")
        user.save()

        EmailAddress.objects.create(
            user=user, email="user@example.com", primary=True, verified=True
        )

        response = self.client.post(
            reverse("account_login"),
            data={"email": "user@example.com", "password": "testerA1234#"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["user"]["email"], "user@example.com")
        self.assertEqual(len(response.data["token"]), 227)

    def test_retrieve_user_profile(self):
        user = self._create_login_user_with_verified_email(user_status=True)
        response = self.client.get(
            reverse("user_profile-detail", args=[user.data["user"]["id"]]),
            data={},
            HTTP_AUTHORIZATION="Bearer {}".format(user.data["token"]),
            format="multipart",
        )
        self.assertEqual(response.status_code, 200)


class TestUserExceptions(TestUsersValid):
    def test_register_with_inadequate_password(self):
        data = {
            "email": "tester@fligt.com",
            "password1": "teste123",
            "password2": "teste123",
            "first_name": "test",
            "last_name": "user",
        }

        response = self.client.post(
            reverse(
                "account_signup",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 400)
        message = "password must be atleast 6 characters, must include numbers, chararcers, uppercase and lowercase character"
        self.assertEqual(response.data["password1"][0], message)

    def test_register_with_non_matching_passwords(self):
        data = {
            "email": "tester@fligt.com",
            "password1": "#tesTe123",
            "password2": "teste123",
            "first_name": "test",
            "last_name": "user",
        }

        response = self.client.post(
            reverse(
                "account_signup",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 400)
        message = "Passwords did not match."
        self.assertEqual(response.data["password2"][0], message)

    def test_login_without_registering(self):
        data = {
            "email": "tester@ya.com",
            "password": "testerA123#",
        }
        response = self.client.post(
            reverse(
                "account_login",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data["non_field_errors"][0],
            "Unable to log in with provided credentials.",
        )

    def test_login_without_email_verification(self):
        self._signup()
        data = {
            "email": "tester@ya.com",
            "password": "testerA123#",
        }
        response = self.client.post(
            reverse(
                "account_login",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data["non_field_errors"][0], "E-mail is not verified."
        )

    def invalid_registration(self):
        data = {
            "email": "tester@ya.com",
            "password": "testerA123#",
        }
        response = self.client.post(
            reverse(
                "account_email_verification_sent",
            ),
            data=data,
        )
        self.assertEqual(response.status_code, 400)

    def invalid_registration_complete_view(self):
        response = self.client.post(
            reverse(
                "account_confirm_complete",
            ),
            data={},
        )
        self.assertEqual(response.status_code, 400)
