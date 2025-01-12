from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode

from config import settings


#  БЛОК ДЛЯ ТОВАРОВ <<<<<<<<<<<<<<<<<<
class Product(models.Model):
    slug = models.SlugField(max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='Слаг')
    title = models.CharField(max_length=100, verbose_name='Товар')
    stock_balance = models.IntegerField(default=0,
                                        verbose_name='Количество')
    manufacturer = models.ForeignKey('Manufacturer',
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     verbose_name='Производитель')
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Category(models.Model):
    """Категория - часы, утюги, холодильники т.п."""

    name = models.CharField(max_length=100, verbose_name='Категория')


class ManufacturerCountry(models.Model):
    """Страна - изготовитель"""

    name = models.CharField(max_length=100, verbose_name='Страна-изготовитель')


class Manufacturer(models.Model):
    """Производитель - название фирмы (Bosh, Armani, etc)"""

    name = models.CharField(max_length=50, verbose_name='Фирма-производитель')
    country = models.ForeignKey('ManufacturerCountry',
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                verbose_name='Страна-изготовитель')


class Photo(models.Model):
    """Фото товара"""

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    photo = models.ImageField(upload_to='products/photo/%Y/%m/%d',
                              blank=True,
                              verbose_name='Фотография')


class PriceChange(models.Model):
    """История изменения цен на товары"""

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    date_price_change = models.DateTimeField(auto_now_add=True,
                                             verbose_name='Дата изменения цены')
    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    verbose_name='Старая цена')
    current_price = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        verbose_name='Текущая цена')


#  БЛОК ДЛЯ ЗАКАЗОВ <<<<<<<<<<<<<<<<<<


class Bill(models.Model):
    """Счет / Покупки """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    store = models.ForeignKey('Store',
                              on_delete=models.DO_NOTHING,
                              verbose_name='Филиал')
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE,
                             verbose_name='Корзина')
    purchase_date = models.DateTimeField(auto_now_add=True,  # дата оплаты
                                         verbose_name='Дата оплаты')

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'
        ordering = ('purchase_date',)


class Store(models.Model):
    """Филиалы"""

    name = models.CharField(max_length=50,
                            verbose_name='Название филиала')
    address = models.CharField(max_length=200,
                               verbose_name='Адрес филиала')


class Cart(models.Model):
    """Корзина"""

    product = models.ForeignKey('Product',
                                default='product has been deleted',
                                on_delete=models.SET_DEFAULT,
                                verbose_name='Товар')
    count = models.IntegerField(default=0,
                                verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('product',)


class Delivries(models.Model):
    """Поставки"""

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    store = models.ForeignKey('Store',
                              on_delete=models.CASCADE,
                              verbose_name='Филиал')
    count = models.IntegerField(default=0,
                                verbose_name='Количество')
    delivery_date = models.DateField(auto_now_add=True,
                                     verbose_name='Дата поставки')


#  ИЗБРАННОЕ <<<<<<<<<<<<<<<<<<

class Favorite(models.Model):
    """Избранное"""

    product = models.ForeignKey('Product',
                                default='product does not exist',
                                on_delete=models.SET_DEFAULT,
                                verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')


#  РЕКЛАМА <<<<<<<<<<<<<<<<<<


class Adv(models.Model):
    """Реклама"""

    adv_type = models.ForeignKey('AdvType',
                                 default='no_category',
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Категория рекламы')
    image = models.ImageField(upload_to='adv/%Y/%m/%d',
                              verbose_name='Рекламный баннер')


class AdvType(models.Model):
    category = models.CharField(max_length=100,
                                verbose_name='Категория рекламы')
