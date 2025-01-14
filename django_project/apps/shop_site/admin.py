from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    exclude = ('slug', )
    # вызовет select_related() для загрузки данных из БД для FK
    # list_select_related = ('manufacturer', 'category')



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('product', 'display_photo', 'photo')
    list_display = ('product',  'id_product', )
    readonly_fields = ('display_photo', )
    search_fields = ('product__id', )
    list_select_related = ('product', )

    @admin.display(description='Фото')
    def display_photo(self, photo: Photo):
        #  mark_safe экранирует теги
        return mark_safe(f'<img src={photo.photo.url} width=50>')

    #Кастомное поле для предпоказа фотки товара
    @admin.display(description='ID', ordering='product_id')
    def id_product(self, photo: Photo):
        return photo.product.id



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
