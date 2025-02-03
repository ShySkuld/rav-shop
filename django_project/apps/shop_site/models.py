import os

import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
import datetime


#  БЛОК ДЛЯ ТОВАРОВ <<<<<<<<<<<<<<<<<<
class Product(models.Model):
    class Status(models.TextChoices):
        SOLD = 'SOLD', 'Распродано'
        PUBLISHED = 'PUB', 'Опубликован'
        PREVIEW = 'PW', 'Черновик'

    slug = models.SlugField(max_length=100,
                            unique=True,
                            db_index=True,
                            verbose_name='Слаг')
    name = models.CharField(max_length=100,
                            verbose_name='Товар')
    subcategory = models.ForeignKey('SubCategory',
                                     default=0,
                                     on_delete=models.SET_DEFAULT,
                                     verbose_name='Подкатегория')
    country = models.ForeignKey('ManufacturerCountry',
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                verbose_name='Страна-изготовитель')
    manufacturer = models.ForeignKey('Manufacturer',
                                     default=0,
                                     on_delete=models.SET_DEFAULT,
                                     blank=True,
                                     verbose_name='Фирма-производитель')
    model = models.CharField(max_length=100,
                             verbose_name='Модель')
    stock_balance = models.IntegerField(default=0,
                                        verbose_name='Количество')
    description = models.TextField(blank=True,
                                   verbose_name='Описание')
    is_published = models.CharField(choices=Status.choices,
                                       default=Status.PREVIEW,
                                       verbose_name="Статус")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-id', )



    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.model))
        self.is_published = 'SOLD' if self.stock_balance == 0 else 'PUB'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID={self.id} -> {self.name} {self.model}'

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Category(models.Model):
    """Общая категория (товары для дома, кухни и т.п.)"""

    name = models.CharField(max_length=100,
                            verbose_name='Категория',
                            unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name', )

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    """Подкатегория для Общей категории"""

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    name = models.CharField(max_length=100,
                            verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Податегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ('name', )

    def __str__(self):
        return self.name


class ManufacturerCountry(models.Model):
    """Страна - изготовитель"""

    name = models.CharField(max_length=100,
                            verbose_name='Страна-изготовитель',
                            unique=True)

    class Meta:
        verbose_name = 'Странa-изготовитель'
        verbose_name_plural = 'Страны-изготовители'
        ordering = ('name', )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    """Производитель - название фирмы (Bosh, Armani, etc)"""

    name = models.CharField(max_length=50,
                            verbose_name='Имя',
                            unique=True)

    class Meta:
        verbose_name = 'Фирма-производитель'
        verbose_name_plural = 'Фирмы-производители'
        ordering = ('name', )

    def __str__(self):
        return self.name



class Photo(models.Model):
    """Фото товара"""

    def set_img_filename(self, full_filename):
        """В виде имени ставлю название товара (product.__str__)
        с добавление в конце id фото. Без проверки аналогичности фото"""
        ext = full_filename.split('.')[-1].lower()  #  расширение

        if ext not in ["jpg", "png", "jpeg"]:  #  проверка расширения
            raise ValidationError(f"invalid image extension: {full_filename}")

        year, month, day = (datetime.datetime.now().year,
                            datetime.datetime.now().month,
                            datetime.datetime.now().day)

        filename = (f'products/photo/{year}/{month}/{day}/'
                    f'{slugify(unidecode(self.product.model))}')

        if self.id:
            return f'{filename}_{self.id}.{ext}'

        else:
            latest_id = Photo.objects.latest('id').id
            return f'{filename}_{latest_id + 1}.{ext}'

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')

    photo = models.ImageField(upload_to=set_img_filename,
                              default='products/photo/korobka.png',
                              verbose_name='Фотография')

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.product.name


class PriceChange(models.Model):
    """История изменения цен на товары"""

    product = models.ForeignKey('Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='price')
    date_price_change = models.DateTimeField(auto_now_add=True,
                                             verbose_name='Дата изменения цены')
    old_price = models.DecimalField(max_digits=10,
                                    decimal_places=0,
                                    default=0,
                                    verbose_name='Старая цена')
    current_price = models.DecimalField(max_digits=10,
                                        decimal_places=0,
                                        default=0,
                                        verbose_name='Текущая цена')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return str(self.product)

#  РЕКЛАМА <<<<<<<<<<<<<<<<<<

class Adv(models.Model):
    """Реклама"""

    adv_type = models.ForeignKey('AdvType',
                                 default='no_category',
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Категория рекламы')
    image = models.ImageField(upload_to='adv/%Y/%m/%d',
                              verbose_name='Рекламный баннер')

    class Meta:
        verbose_name = 'Рекламное объявление'
        verbose_name_plural = 'Рекламные объявления'


class AdvType(models.Model):
    category = models.CharField(max_length=100,
                                verbose_name='Категория рекламы')

    class Meta:
        verbose_name = 'Категорию рекламы'
        verbose_name_plural = 'Категории рекламы'
