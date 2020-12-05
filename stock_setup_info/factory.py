from faker.providers import internet, lorem
import factory
from stock_setup_info.models import (
    Industry,
    StockManagement,
    StructureType,
    Structure,
    Stock,
    SubSector,
    MainSector,
)
from faker import Faker, Factory

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(lorem)


class RecursiveClass:
    def __init__(self, child):
        self.child = child


class RecursiveFactory(factory.Factory):
    class Meta:
        model = RecursiveClass
        exclude = ("child_depth_temp",)

    class Params:
        child_depth = 10

    child_depth_temp = factory.LazyAttribute(lambda o: o.child_depth - 1)
    child = factory.Maybe(
        factory.LazyAttribute(lambda o: o.child_depth > 0),
        yes_declaration=factory.SubFactory(
            "stock_setup_info.factory.RecursiveFactory",
            child_depth=factory.SelfAttribute("..child_depth_temp"),
        ),
        no_declaration=None,
    )


class IndustryFactory(factory.DjangoModelFactory):
    name = faker.name()
    exchange_code = faker.text(max_nb_chars=10, ext_word_list=None)
    sync_flag = faker.boolean(chance_of_getting_true=50)
    logo = faker.text(max_nb_chars=10, ext_word_list=None)

    class Meta:
        model = Industry


class MainSectorFactory(factory.DjangoModelFactory):
    name = faker.name()
    is_active = faker.boolean(chance_of_getting_true=50)

    class Meta:
        model = MainSector


class SubSectorFactory(factory.DjangoModelFactory):
    name = faker.name()
    is_active = faker.boolean(chance_of_getting_true=50)
    main_sector = factory.SubFactory(MainSector)

    class Meta:
        model = SubSector


class StructureTypeFactory(factory.DjangoModelFactory):
    structure_type_name = faker.text(max_nb_chars=10, ext_word_list=None)
    description = faker.sentence(100)
    is_active = faker.boolean(chance_of_getting_true=50)
    parent = factory.SubFactory("stock_setup_info.factory.StructureTypeFactory")

    class Meta:
        model = StructureType
        exclude = ("child_depth_temp",)

    class Params:
        child_depth = 10

    child_depth_temp = factory.LazyAttribute(lambda o: o.child_depth - 1)
    parent = factory.Maybe(
        factory.LazyAttribute(lambda o: o.child_depth > 0),
        yes_declaration=factory.SubFactory(
            "stock_setup_info.factory.StructureTypeFactory",
            child_depth=factory.SelfAttribute("..child_depth_temp"),
        ),
        no_declaration=None,
    )


class StructureFactory(factory.DjangoModelFactory):
    structure_name = faker.text(max_nb_chars=10, ext_word_list=None)
    structure_code = faker.text(max_nb_chars=10, ext_word_list=None)
    structure_type = factory.SubFactory(StructureTypeFactory)
    parent = factory.SubFactory("stock_setup_info.factory.StructureFactory")
    is_active = faker.boolean(chance_of_getting_true=50)
    comment = faker.sentence(15)

    class Meta:
        model = Structure
        exclude = ("child_depth_temp",)

    class Params:
        child_depth = 10

    child_depth_temp = factory.LazyAttribute(lambda o: o.child_depth - 1)
    parent = factory.Maybe(
        factory.LazyAttribute(lambda o: o.child_depth > 0),
        yes_declaration=factory.SubFactory(
            "stock_setup_info.factory.StructureFactory",
            child_depth=factory.SelfAttribute("..child_depth_temp"),
        ),
        no_declaration=None,
    )


class StockFactory(factory.DjangoModelFactory):
    id = faker.random_number()
    stock_code = faker.text(max_nb_chars=20, ext_word_list=None)
    name = faker.text(max_nb_chars=20, ext_word_list=None)
    exchange_code = faker.text(max_nb_chars=20, ext_word_list=None)
    asset_class_code = faker.text(max_nb_chars=20, ext_word_list=None)
    contact = faker.text(max_nb_chars=20, ext_word_list=None)
    description = faker.text(max_nb_chars=20, ext_word_list=None)
    tier_code = faker.text(max_nb_chars=20, ext_word_list=None)
    par_value = faker.text(max_nb_chars=20, ext_word_list=None)
    list_date = faker.date()
    outstanding_shares = faker.random_number()
    grp_code = faker.text(max_nb_chars=20, ext_word_list=None)
    registrar = faker.text(max_nb_chars=20, ext_word_list=None)
    address_1 = faker.text(max_nb_chars=20, ext_word_list=None)
    address_2 = faker.text(max_nb_chars=20, ext_word_list=None)
    address_3 = faker.text(max_nb_chars=20, ext_word_list=None)
    state_code = faker.text(max_nb_chars=20, ext_word_list=None)
    website = faker.uri()
    email = faker.company_email()
    gsm = faker.text(100)
    land_tel = faker.text(max_nb_chars=20, ext_word_list=None)
    fax_no = faker.text(max_nb_chars=20, ext_word_list=None)
    regis_close = faker.date()
    year_end = faker.text(max_nb_chars=20, ext_word_list=None)
    logo = faker.text(max_nb_chars=20, ext_word_list=None)
    shares_in_issue = faker.random_number()
    capitalization = faker.random_number()
    view_count = faker.random_number()
    industry = factory.SubFactory(IndustryFactory)
    structure = factory.SubFactory(StructureFactory)
    is_active = faker.boolean()

    class Meta:
        model = Stock


class StockManagementFactory(factory.DjangoModelFactory):
    name = faker.text(100)
    position = faker.text(100)
    management_type = faker.random_elements(
        elements=("directors", "management", "staff"), length=1, unique=False
    )
    is_active = faker.boolean()

    class Meta:
        model = StockManagement
