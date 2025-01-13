from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug', )
    # вызовет select_related() для загрузки данных из БД для FK
    # list_select_related = ('manufacturer', 'category')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceChange)
class PriceChangeAdmin(admin.ModelAdmin):
    pass


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvType)
class AdvTypeAdmin(admin.ModelAdmin):
    pass
