from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'manufacturer', 'model',
                    'stock_balance', 'get_product_price', 'is_published')
    list_display_links = ('model', )
    exclude = ('slug', 'name')
    list_filter = ('manufacturer', 'is_published')
    search_fields = ('model', )
    list_editable = ('is_published', )
    list_per_page = 8

    # вызовет select_related() для загрузки данных из БД для FK
    list_select_related = ('country', 'manufacturer', 'subcategory')

    #  кастомное поле с ценой товара
    def get_product_price(self, product: Product):
        """product - <class 'apps.shop_site.models.Product'>
        Как я понял, отрисовывает построчно, каждый раз обращаясь
        к этой функции с разными объектми Product.
        Возвращаю последнее изменение цены из кверисета всех изменений для
        конкретного товара"""
        if product.price.exists():
            return [prices.current_price for prices in product.price.all()][-1]
        return 0

    get_product_price.short_description = "Цена"


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('product', 'display_photo', 'photo')
    list_display = ('id_product', 'display_photo', 'product_name')
    list_display_links = ('product_name', )

    readonly_fields = ('display_photo', 'id')
    search_fields = ('product__id', )
    list_select_related = ('product', )

    #Кастомное поле для предпоказа фотки товара
    @admin.display(description='Фото')
    def display_photo(self, photo: Photo):
        #  mark_safe экранирует теги
        return mark_safe(f'<img src={photo.photo.url} width=50>')

    @admin.display(description='ID')
    def id_product(self, photo: Photo):
        return photo.product.id

    @admin.display(description='Товар')
    #  не знаю как перекастомизировать имя, пока прикручу это поле
    def product_name(self, photo: Photo):
        return f'{photo.product.subcategory} {photo.product.model}'


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(PriceChange)
class PriceChangeAdmin(admin.ModelAdmin):
    list_display = ('product', 'date_price_change', 'old_price','current_price')
    ordering = ('-date_price_change', )


@admin.register(Adv)
class AdvAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvType)
class AdvTypeAdmin(admin.ModelAdmin):
    pass
