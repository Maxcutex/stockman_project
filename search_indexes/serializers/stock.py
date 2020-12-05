import json

from rest_framework import serializers


class StockDocumentSerializer(serializers.Serializer):
    """Serializer for the Stock document."""

    id = serializers.IntegerField()
    stock_code = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    exchange_code = serializers.CharField(read_only=True)
    asset_class_code = serializers.CharField(read_only=True)
    contact = serializers.CharField(read_only=True)
    registrar = serializers.CharField(read_only=True)
    year_end = serializers.CharField(read_only=True)
    logo = serializers.CharField(read_only=True)
    shares_in_issue = serializers.IntegerField(read_only=True)
    capitalization = serializers.IntegerField(read_only=True)

    industry = serializers.CharField(read_only=True)

    sub_sector = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    class Meta(object):
        """Meta options."""

        fields = (
            "id",
            "stock_code",
            "name",
            "description",
            "exchange_code",
            "asset_class_code",
            "contact",
            "registrar",
            "year_end",
            "logo",
            "shares_in_issue",
            "capitalization",
            "industry",
            "sub_sector",
            "is_active",
        )
        read_only_fields = fields
