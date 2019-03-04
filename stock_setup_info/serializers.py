from rest_framework import serializers
from rest_framework.settings import api_settings
from enumchoicefield import ChoiceEnum, EnumChoiceField
from .models import (Industry, Structure, StructureType,
                     Stock, StockManagement, ManagementType)
from stockman_project import settings


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('id','name', 'exchange_code', 'sync_flag', 'logo')
        ordering_fields = ('id',)
        ordering = ['-id']


class StructureSerializer(serializers.ModelSerializer):
    # structure_type_name = serializers.PrimaryKeyRelatedField(
    #     source='structure_type.structure_type_name', read_only=True)

    class Meta:
        model = Structure
        fields = (
            'id', 'structure_name', 'structure_code',
            'is_active', 'structure_type_id', 'structure_type',  # 'structure_type_name',
            'parent_id'
        )
        ordering_fields = ('id',)
        ordering = ['-id']


class StructureTypeSerializer(serializers.ModelSerializer):
    # parent_structure_type = StructureTypeSerializer(read_only=True)
    child_structures = StructureSerializer(many=True, read_only=True)

    class Meta:
        model = StructureType
        fields = ('id', 'structure_type_name',
                  'is_active', 'description',   'parent_id', 'child_structures')
        ordering_fields = ('id',)
        ordering = ['-id']


class StockManagementSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockManagement
        fields = ('id', 'name', 'position', 'management_type')
        ordering_fields = ('id',)
        ordering = ['-id']


class StockSerializer(serializers.ModelSerializer):
    list_date = serializers.DateField(input_formats=[('%mm-%dd-%yyyy', 'iso-8601')])
    regis_close = serializers.DateField(input_formats=[('%Y-%m-%d', 'iso-8601')])
    filter_fields = ('description', 'stock_code', 'name')

    class Meta:
        model = Stock
        fields = ('id', 'name', 'stock_code',
                  'is_active', 'exchange_code', 'contact',
                  'description', 'tier_code', 'par_value',
                  'asset_class_code', 'list_date', 'outstanding_shares',
                  'grp_code', 'registrar', 'address_1',
                  'address_2', 'address_3', 'state_code',
                  'website', 'email', 'gsm',
                  'land_tel', 'fax_no', 'regis_close',
                  'year_end', 'logo', 'shares_in_issue',
                  'capitalization', 'industry', 'structure'
                  )
        ordering_fields = ('id',)
        ordering = ['-id']
