from django.db import models

from config import settings
from apps.shop_site.models import Product


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

    product = models.ForeignKey(Product,
                                default='product has been deleted',
                                on_delete=models.SET_DEFAULT,
                                verbose_name='Товар')
    count = models.IntegerField(default=0,
                                verbose_name='Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ('product',)


class Deliveries(models.Model):
    """Поставки"""

    product = models.ForeignKey(Product,
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

    product = models.ForeignKey(Product,
                                default='product does not exist',
                                on_delete=models.SET_DEFAULT,
                                verbose_name='Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
