import tempfile
from io import StringIO, BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import File
from PIL import Image
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import random
from faker.providers import internet, lorem
import factory
from faker import Factory

# python manage.py seed --mode=refresh
from django.db.backends.utils import logger

from stock_maintain.models import (
    PriceList,
    News,
    AnalysisCategorySection,
    AnalysisOpinion,
    NewsCategorySection,
    NewsImage,
    AnalysisImage,
    SiteAuthor,
)
from stock_setup_info.models import (
    StructureType,
    Structure,
    Industry,
    Stock,
    SectionGroup,
)

MODE_CLEAR = "clear"

faker = Factory.create()
faker.add_provider(internet)
faker.add_provider(lorem)


def get_image_file(name="test.png", ext="png", size=(50, 50), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", default="clear", type=str, help="Mode")
        parser.add_argument("--records", default=15, type=int, help="Records number")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Structure instances")
    Structure.objects.all().delete()
    logger.info("Delete StructureType instances")
    StructureType.objects.all().delete()
    logger.info("Delete Industry instances")
    Industry.objects.all().delete()
    logger.info("Delete Price instances")
    PriceList.objects.all().delete()
    logger.info("Delete Stock instances")
    Stock.objects.all().delete()
    logger.info("Delete News instances")
    News.objects.all().delete()
    logger.info("Delete NewsImages instances")
    NewsImage.objects.all().delete()
    logger.info("Delete News Sections instances")
    NewsCategorySection.objects.all().delete()
    logger.info("Delete Analysis instances")
    AnalysisOpinion.objects.all().delete()
    logger.info("Delete Analysis Images instances")
    AnalysisImage.objects.all().delete()
    logger.info("Delete Analysis Sections instances")
    AnalysisCategorySection.objects.all().delete()


def create_industy():
    industry = Industry(
        name=faker.name(),
        exchange_code=faker.text(max_nb_chars=10, ext_word_list=None),
        sync_flag=faker.boolean(chance_of_getting_true=50),
        logo=faker.text(max_nb_chars=10, ext_word_list=None),
    )
    industry.save()
    logger.info("{} industry created.".format(industry))
    return industry


def create_structure_type():
    structure_type = StructureType(
        structure_type_name="SECTOR",
        description=faker.sentence(100),
        is_active=True,
        parent=None,
    )
    structure_type.save()
    logger.info("{} structure type created.".format(structure_type))
    structure_type1 = StructureType(
        structure_type_name="NEWS SECTIONS",
        description=faker.sentence(100),
        is_active=True,
        parent=None,
    )
    structure_type1.save()
    logger.info("{} structure type created.".format(structure_type1))
    return structure_type, structure_type1


def create_structure(structure_type):
    structure = Structure(
        structure_name="AGRICULTURE",
        structure_code=None,
        structure_type=structure_type,
        parent=None,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure.save()
    structure2 = Structure(
        structure_name="CONGLOMERATES",
        structure_code=None,
        structure_type=structure_type,
        parent=None,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure2.save()
    structure3 = Structure(
        structure_name="CONSTRUCTION/REAL ESTATE",
        structure_code=None,
        structure_type=structure_type,
        parent=None,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure3.save()
    structure4 = Structure(
        structure_name="CONSUMER GOODS",
        structure_code=None,
        structure_type=structure_type,
        parent=None,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure4.save()
    structure = Structure(
        structure_name="Crop Production",
        structure_code=None,
        structure_type=structure_type,
        parent=structure,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure.save()
    structure = Structure(
        structure_name="Diversified Industries",
        structure_code=None,
        structure_type=structure_type,
        parent=structure2,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure.save()
    structure = Structure(
        structure_name="Real Estate Development",
        structure_code=None,
        structure_type=structure_type,
        parent=structure3,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure.save()
    structure = Structure(
        structure_name="Beverages-Non Alcoholic",
        structure_code=None,
        structure_type=structure_type,
        parent=structure4,
        is_active=True,
        comment=faker.sentence(15),
    )
    structure.save()
    logger.info("{} structures created.".format(structure))
    return structure, structure2


def create_stock(industry, structure):
    stock = Stock(
        stock_code="7UP",
        name="7-UP BOTTLING COMPANY PLS",
        exchange_code="C",
        asset_class_code="EG",
        contact="SEVEN UP",
        description=faker.text(max_nb_chars=20, ext_word_list=None),
        tier_code="7UP",
        par_value="0.5",
        list_date=faker.date(),
        outstanding_shares=234234234,
        grp_code=faker.text(max_nb_chars=20, ext_word_list=None),
        registrar=faker.text(max_nb_chars=20, ext_word_list=None),
        address_1=faker.text(max_nb_chars=20, ext_word_list=None),
        address_2=faker.text(max_nb_chars=20, ext_word_list=None),
        address_3=faker.text(max_nb_chars=20, ext_word_list=None),
        state_code=faker.text(max_nb_chars=20, ext_word_list=None),
        website=faker.uri(),
        email=faker.company_email(),
        gsm=faker.text(100),
        land_tel=faker.text(max_nb_chars=20, ext_word_list=None),
        fax_no=faker.text(max_nb_chars=20, ext_word_list=None),
        regis_close=faker.date(),
        year_end=faker.text(max_nb_chars=20, ext_word_list=None),
        logo=faker.text(max_nb_chars=20, ext_word_list=None),
        shares_in_issue=faker.random_number(),
        capitalization=faker.random_number(),
        view_count=faker.random_number(),
        industry=industry,
        structure=structure,
        is_active=faker.boolean(),
    )
    stock.save()
    logger.info("{} stock created.".format(stock))
    return stock


def create_price_list(stock):
    price_item = PriceList(
        sec_code="7UP",
        price_date=faker.date(),
        price_close=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        x_open=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        x_high=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        x_low=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        price=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        x_change=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        offer_bid_sign="+",
        num_of_deals=faker.random_number(),
        volume=faker.random_number(),
        x_value=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        dps=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        eps=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        pe=faker.pydecimal(left_digits=None, right_digits=2, positive=True),
        rpt=faker.text(10),
        e_time=faker.date(),
        e_date=faker.date(),
        source=faker.text(10),
        sync_flag=faker.random_number(),
        stock=stock,
    )
    price_item.save()
    logger.info("{} price list created.".format(price_item))
    return price_item


def create_news(stock, section, section2):
    author = SiteAuthor(
        image_file=get_image_file(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        description=faker.sentence(
            nb_words=6, variable_nb_words=True, ext_word_list=None
        ),
        twitter=faker.name(),
        facebook=faker.name(),
        linked_in=faker.name(),
        email=faker.name(),
    )
    news = News(
        title=faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
        content=faker.paragraphs(nb=3, ext_word_list=None),
        news_date=faker.date(),
        entry_date=faker.date(),
        stock=stock,
        is_featured=faker.boolean(),
        has_downloadable=faker.boolean(),
        is_main=faker.boolean(),
        author=author,
    )
    news.save()
    create_news_images(news)
    create_news_section(news, section)
    create_news_section(news, section2)
    news1 = News(
        title=faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
        content=faker.paragraphs(nb=3, ext_word_list=None),
        news_date=faker.date(),
        entry_date=faker.date(),
        stock=stock,
        is_featured=faker.boolean(),
        has_downloadable=faker.boolean(),
        is_main=faker.boolean(),
        author=author,
    )
    news1.save()
    create_news_images(news1)
    create_news_section(news1, section)
    create_news_section(news1, section2)
    logger.info("{} news created.".format(news1))
    return news


def create_news_images(news):
    news_images = NewsImage(
        news=news,
        is_main=faker.boolean(),
        name=faker.text(10),
        image_type="size300x200",
        image_file=get_image_file(),
    )
    news_images.save()


def create_news_section(news, section):
    news_section = NewsCategorySection(news=news, section=section)
    news_section.save()


def create_analysis(structure):
    analysis = AnalysisOpinion(
        title=faker.text(100),
        content=faker.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
        opinion_date=faker.date_this_decade(before_today=True, after_today=False),
        entry_date=faker.date_this_decade(before_today=True, after_today=False),
        author=faker.text(10),
    )
    analysis.save()
    create_analysis_section(analysis, structure)
    create_analysis_images(analysis)


def create_analysis_section(analysis, section):
    analysis_section = AnalysisCategorySection(analysis=analysis, section=section)
    analysis_section.save()


def create_analysis_images(analysis):
    analysis_images = AnalysisImage(
        analysis=analysis,
        is_main=faker.boolean(),
        name=faker.text(10),
        image_type="size300x200",
        image_file=get_image_file(),
    )
    analysis_images.save()


def create_market_indices():
    pass


def create_section_group():
    if SectionGroup.objects.count() == 0:
        section_group = SectionGroup(section_name="World")
        section_group.save()
        section_group1 = SectionGroup(section_name="Money")
        section_group1.save()
        section_group11 = SectionGroup(section_name="Life")
        section_group11.save()
        section_group111 = SectionGroup(section_name="Economy")
        section_group111.save()
        section_group2 = SectionGroup(section_name="Business")
        section_group2.save()
        section_group21 = SectionGroup(section_name="Politics")
        section_group21.save()
        section_group211 = SectionGroup(section_name="Markets")
        section_group211.save()
        section_group2111 = SectionGroup(section_name="Art")
        section_group2111.save()


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    # clear_data()
    if mode == MODE_CLEAR:
        return
    # industry = create_industy()
    # structure_type, structure_type1 = create_structure_type()
    # structure, structure2 = create_structure(structure_type)
    # stock = create_stock(industry, structure)
    # create_price_list(stock)
    # create_news(stock, structure, structure2)
    # create_analysis(structure)
    # create_market_indices()
    create_section_group()
