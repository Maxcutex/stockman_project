from rest_framework import serializers
from .models import Industry, Structure, StructureType


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ('name', 'exchange_code', 'sync_flag', 'logo')


class StructureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructureType
        fields = ('structure_type_name', 'parent_id',
                  'is_active', 'description')


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ('structure_name', 'structure_type_id',
                  'parent_id', 'is_active')
