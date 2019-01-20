import factory
from faker.providers import internet, person

from faker import Faker, Factory

from stock_profile_mgt.models import UserProfile

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(person)


class UserProfileFactory(factory.DjangoModelFactory):
	email = faker.safe_email()
	first_name = faker.first_name()
	last_name = faker.last_name()
	is_active = faker.boolean()
	is_staff = faker.boolean()

	class Meta:
		model = UserProfile
