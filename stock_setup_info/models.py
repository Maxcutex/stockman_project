from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from model_utils import Choices


class Industry(models.Model):
	name = models.CharField(max_length=100)
	exchange_code = models.CharField(max_length=50)
	sync_flag = models.CharField(max_length=30)
	logo = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class StructureType(models.Model):
	structure_type_name = models.CharField(max_length=100)
	description = models.CharField(max_length=2000, null=True, blank=True)
	is_active = models.BooleanField(max_length=100)
	parent_id = models.ForeignKey(
		'self', null=True, on_delete=models.CASCADE,
		related_name='child_structure_type'
	)

	def __str__(self):
		return self.structure_type_name


class Structure(models.Model):
	structure_name = models.CharField(max_length=100)
	structure_code = models.CharField(max_length=50, null=True, blank=True)
	structure_type = models.ForeignKey(
		StructureType, on_delete=models.CASCADE, related_name='child_structures')
	parent_id = models.ForeignKey(
		'self', null=True, on_delete=models.CASCADE, related_name='structures')
	is_active = models.BooleanField()
	comment = models.CharField(max_length=200)

	def __str__(self):
		return self.structure_name


class Stock(models.Model):
	stock_code = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	exchange_code = models.CharField(max_length=50)
	asset_class_code = models.CharField(max_length=50)
	contact = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	tier_code = models.CharField(max_length=50)
	par_value = models.CharField(max_length=50)
	list_date = models.DateField(blank=True, null=True)
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
	regis_close = models.DateField(blank=True, null=True)
	year_end = models.CharField(max_length=50)
	logo = models.CharField(max_length=50)
	shares_in_issue = models.BigIntegerField()
	capitalization = models.BigIntegerField()
	view_count = models.BigIntegerField(default=0)
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
	management_choice = Choices('management', 'director')
	name = models.CharField(max_length=250)
	position = models.CharField(max_length=250)
	management_type = models.CharField(
		choices=management_choice, default=management_choice.management, max_length=30)
	is_active = models.BooleanField()

	def __str__(self):
		return self.name
