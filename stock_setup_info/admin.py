from admin_ordering.admin import OrderableAdmin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    Industry,
    Stock,
    Structure,
    StructureType,
    StockManagement,
    SubSector,
    MainSector,
)

# Register your models here.

admin.site.register(Industry)


@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin, OrderableAdmin, admin.ModelAdmin):
    model = Stock
    search_fields = ("stock_code",)
    ordering_field = "stock_code"


admin.site.register(Structure)
admin.site.register(StructureType)
admin.site.register(StockManagement)
admin.site.register(MainSector)
admin.site.register(SubSector)
