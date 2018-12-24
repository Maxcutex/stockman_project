from rest_framework import serializers
from .models import Industry, Structure, StructureType


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
    class Meta:
        model = Structure
        fields = ('id', 'structure_name', 'structure_code',
                  'is_active', 'structure_type', 'url', 'structures')
