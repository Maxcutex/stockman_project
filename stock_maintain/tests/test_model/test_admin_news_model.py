import pdb

from django.contrib.admin import AdminSite
from mixer.auto import mixer
from nose.tools import set_trace
from stock_maintain import admin, models
from stock_setup_info.factory import (
    StructureTypeFactory,
    StructureFactory,
    StockFactory,
    MainSectorFactory,
    SubSectorFactory,
)


class TestNewsAdmin:
    def setUp(self):
        self.main_sector = MainSectorFactory()
        self.sub_sector = SubSectorFactory(main_sector=self.main_sector)
        self.stock = mixer.blend(
            "stock_setup_info.models.Stock", sub_sector=self.sub_sector
        )
        self.news = mixer.blend(
            "stock_maintain.models.News",
            content="Hello this is the main news",
            stock=self.stock,
        )

    # def test_news_excerpt(self):
    # 	site = AdminSite()
    # 	news_admin = admin.NewsAdmin(models.News, site)
    # 	result = news_admin.newstitle(self.news)
    # 	assert result == 'Hello', 'Should return first few characters'
