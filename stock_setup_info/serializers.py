from rest_framework import serializers
from .models import Industry, Structure, StructureType, Stock


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Industry
        fields = ('name', 'exchange_code', 'sync_flag', 'logo', 'url')


class StructureTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StructureType
        fields = ('id', 'structure_type_name',
                  'is_active', 'description', 'url', 'structure_types')


class StructureSerializer(serializers.HyperlinkedModelSerializer):
    structure_type_id = serializers.PrimaryKeyRelatedField(read_only=True)
    structure_type = serializers.PrimaryKeyRelatedField(
        source='structure_type.structure_type_name', read_only=True)

    class Meta:
        model = Structure
        fields = ('id', 'structure_name', 'structure_code',
                  'is_active', 'structure_type_id', 'structure_type', 'url', 'structures')


class StockSerializer(serializers.ModelSerializer):

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
