from django.contrib import admin
from .models import Industry, Stock, Structure, StructureType, StockManagement, SubSector, MainSector

# Register your models here.

admin.site.register(Industry)
admin.site.register(Stock)
admin.site.register(Structure)
admin.site.register(StructureType)
admin.site.register(StockManagement)
admin.site.register(MainSector)
admin.site.register(SubSector)
