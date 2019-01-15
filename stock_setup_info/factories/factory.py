from faker.providers import internet
import factory
from stock_setup_info.models import Industry, StockManagement, StructureType, Structure, Stock
from faker import Faker, Factory

faker = Factory.create()
faker.add_provider(internet)


class IndustryFactory(factory.DjangoModelFactory):
	name = faker.name()
	exchange_code = faker.text(10)
	sync_flag = faker.text(10)
	logo = faker.text(10)

	class Meta:
		model = Industry


class StructureTypeFactory(factory.DjangoModelFactory):
	structure_type_name = faker.text(10)
	description = faker.sentence(100)
	is_active = faker.boolean(chance_of_getting_true=50)
	parent_id = factory.SubFactory('stock_setup_info.factories.StructureTypeFactory')

	class Meta:
		model = StructureType


class StructureFactory(factory.DjangoModelFactory):
	structure_name = faker.text(10)
	structure_code = faker.text(10)
	structure_type = factory.SubFactory(StructureTypeFactory)
	parent_id = factory.SubFactory('stock_setup_info.factories.StructureFactory')
	is_active = faker.boolean(chance_of_getting_true=50)
	comment = faker.sentence(100)

	class Meta:
		model = Structure


class StockFactory(factory.DjangoModelFactory):
	stock_code = faker.text(10)
	name = faker.text(10)
	exchange_code = faker.text(10)
	asset_class_code = faker.text(10)
	contact = faker.text(10)
	description = faker.text(10)
	tier_code = faker.text(10)
	par_value = faker.text(10)
	list_date = faker.date()
	outstanding_shares = faker.text(10)
	grp_code = faker.text(10)
	registrar = faker.text(10)
	address_1 = faker.text(10)
	address_2 = faker.text(10)
	address_3 = faker.text(10)
	state_code = faker.text(10)
	website = faker.text(100)
	email = faker.text(100)
	gsm = faker.text(100)
	land_tel = faker.text(10)
	fax_no = faker.text(10)
	regis_close = faker.date()
	year_end = faker.text(10)
	logo = faker.text(10)
	shares_in_issue = faker.random_number()
	capitalization = faker.random_number()
	view_count =faker.random_number()
	industry = factory.SubFactory(IndustryFactory)
	structure = factory.SubFactory(StructureFactory)
	is_active = faker.boolean()

	class Meta:
		model = Stock


class StockManagementFactory(factory.DjangoModelFactory):
	name = faker.text(100)
	position = faker.text(100)
	management_type = faker.random_elements(elements=('directors', 'management', 'staff'), length=1, unique=False)
	is_active = faker.boolean()

	class Meta:
		model = StockManagement
