from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField


class Industry(models.Model):
    name = models.CharField(max_length=100)
    exchange_code = models.CharField(max_length=50)
    sync_flag = models.CharField(max_length=30)
    logo = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class StructureType(models.Model):
    structure_type_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(max_length=100)
    parent_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.structure_type_name


# class StructureTypeRelationship(models.Model):
#     from_structure_type = models.ForeignKey(
#         'StructureType', related_name='from_structure_types', on_delete=models.CASCADE)
#     to_structure_type = models.ForeignKey(
#         'StructureType', related_name='to_structure_types', on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('from_structure_type', 'to_structure_type')


class Structure(models.Model):
    structure_name = models.CharField(max_length=100)
    structure_code = models.CharField(max_length=50, null=True, blank=True)
    structure_type = models.ForeignKey(
        StructureType, on_delete=models.CASCADE, related_name='structures')
    parent_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.structure_name


# class StructureRelationship(models.Model):
#     from_structure = models.ForeignKey(
#         'Structure', related_name='from_structures', on_delete=models.CASCADE)
#     to_structure = models.ForeignKey(
#         'Structure', related_name='to_structures', on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('from_structure', 'to_structure')


class Stock(models.Model):
    stock_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    exchange_code = models.CharField(max_length=50)
    asset_class_code = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tier_code = models.CharField(max_length=50)
    par_value = models.CharField(max_length=50)
    list_date = models.DateField(max_length=50)
    outstanding_shares = models.CharField(max_length=50)
    grp_code = models.CharField(max_length=50)
    registrar = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    address_3 = models.CharField(max_length=50)
    state_code = models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    gsm = models.CharField(max_length=150)
    land_tel = models.CharField(max_length=50)
    fax_no = models.CharField(max_length=50)
    regis_close = models.DateField(max_length=50)
    year_end = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)
    shares_in_issue = models.BigIntegerField()
    capitalization = models.BigIntegerField()
    view_count = models.BigIntegerField()
    industry = models.ForeignKey(
        Industry, on_delete=models.CASCADE, related_name='stocks')
    structure = models.ForeignKey(
        Structure, on_delete=models.CASCADE, related_name='stock_structure')
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class ManagementType(ChoiceEnum):
    management = "management"
    director = "director"


class StockManagement(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    management_type = EnumChoiceField(
        enum_class=ManagementType, default=ManagementType.management)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
