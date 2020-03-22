from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models, connection
from enumchoicefield import ChoiceEnum, EnumChoiceField
from model_utils import Choices


class Industry(models.Model):
    name = models.CharField(max_length=100)
    exchange_code = models.CharField(max_length=50, null=True)
    sync_flag = models.BooleanField(default=False)
    logo = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class MainSector(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class SubSector(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    main_sector = models.ForeignKey(
        MainSector, on_delete=models.CASCADE, related_name='sub_sector_main_sector')

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class StructureType(models.Model):
    structure_type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, null=True, blank=True)
    is_active = models.BooleanField(max_length=100)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE,
        related_name='child_structure_type'
    )

    def __str__(self):
        return self.structure_type_name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class SectionGroup(models.Model):
    section_name = models.CharField(max_length=100)

    def __str__(self):
        return self.section_name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class Structure(models.Model):
    structure_name = models.CharField(max_length=100)
    structure_code = models.CharField(max_length=50, null=True, blank=True)
    structure_type = models.ForeignKey(
        StructureType, on_delete=models.CASCADE, related_name='child_structures')
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name='structures')
    is_active = models.BooleanField(default=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.structure_name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class Stock(models.Model):
    stock_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    exchange_code = models.CharField(max_length=50, null=True)
    asset_class_code = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=300, blank=True, null=True)
    description  = RichTextUploadingField( blank=True, null=True)
    tier_code = models.CharField(max_length=50, blank=True, null=True)
    par_value = models.CharField(max_length=50, blank=True, null=True)
    list_date = models.DateField(blank=True, null=True)
    outstanding_shares = models.DecimalField(null=True, max_digits=19, decimal_places=2)
    grp_code = models.CharField(max_length=50, blank=True, null=True)
    registrar = models.CharField(max_length=50, blank=True, null=True)
    address_1 = models.CharField(max_length=50, blank=True, null=True)
    address_2 = models.CharField(max_length=50, blank=True, null=True)
    address_3 = models.CharField(max_length=50, blank=True, null=True)
    state_code = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    gsm = models.CharField(max_length=150, blank=True, null=True)
    land_tel = models.CharField(max_length=50, blank=True, null=True)
    fax_no = models.CharField(max_length=50, blank=True, null=True)
    regis_close = models.DateField(blank=True, null=True)
    year_end = models.CharField(max_length=50, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)
    shares_in_issue = models.BigIntegerField(default=0, null=True)
    capitalization = models.BigIntegerField(default=0, null=True)
    view_count = models.BigIntegerField(default=0, null=True)
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name='stocks')
    sub_sector = models.ForeignKey(
        SubSector, on_delete=models.CASCADE, related_name='stock_sub_sector',null=True,default=None)
    is_active = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.stock_code

    @property
    def industry_indexing(self):
        """industry for indexing.		Used in Elasticsearch indexing.		"""
        if self.industry is not None:
            return self.industry.name

    @property
    def sub_sector_indexing(self):
        """subsector for indexing. Used in Elasticsearch indexing. """
        if self.sub_sector is not None:
            return self.sub_sector.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class ManagementType(ChoiceEnum):
    management = "management"
    director = "director"


class StockManagement(models.Model):
    management_choice = Choices('management', 'director')
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    management_type = models.CharField(
        choices=management_choice, default=management_choice.management, max_length=30)
    is_active = models.BooleanField()
    stock = models.ForeignKey(
        Stock, on_delete=models.CASCADE, related_name='management_stock')

    def __str__(self):
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))
