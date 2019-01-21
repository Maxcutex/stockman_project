import factory
from faker.providers import internet, person
from faker import Faker, Factory

from stock_profile_mgt.models import UserProfile

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(person)


def _create_user(self, email='johndoe@gmail.com', password='tester123'):
    user = UserProfile.objects.create(
        email=email, password=password,
        is_active=True)
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
    user.save()
    return user


class UserProfileFactory(factory.DjangoModelFactory):
	email = faker.safe_email()
	first_name = faker.first_name()
	last_name = faker.last_name()
	is_active = faker.boolean()
	is_staff = faker.boolean()

	class Meta:
		model = UserProfile
