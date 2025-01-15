from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'manufacturer', 'model', 'get_product_price')
    exclude = ('slug', 'name')
    list_filter = ('manufacturer', )

    # вызовет select_related() для загрузки данных из БД для FK
    list_select_related = ('country', 'manufacturer', 'subcategory')

    #  кастомное поле с ценой товара
    def get_product_price(self, product: Product):
        """product - <class 'apps.shop_site.models.Product'>
        Как я понял, отрисовывает построчно, каждый раз обращаясь
        к этой функции с разными объектми Product.
        Возвращаю последнее изменение цены из кверисета всех изменений для
        конкретного товара"""

        return [prices.current_price for prices in product.price.all()][-1]

    get_product_price.short_description = "Цена"

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('product', 'display_photo', 'photo')
    list_display = ('product_name', 'id_product')

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

    @admin.display(description='Товар', ordering='product_id')
    #  не знаю как перекастомизировать имя, пока прикручу это поле
    def product_name(self, photo: Photo):
        return f'{photo.product.name} {photo.product.model}'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name', )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')


@admin.register(ManufacturerCountry)
class ManufacturerCountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceChange)
class PriceChangeAdmin(admin.ModelAdmin):
    list_display = ('product', 'date_price_change', 'old_price', 'current_price')
    ordering = ('-date_price_change', )


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvType)
class AdvTypeAdmin(admin.ModelAdmin):
    pass
