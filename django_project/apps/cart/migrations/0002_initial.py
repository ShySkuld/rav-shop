# Generated by Django 5.1.4 on 2025-01-14 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        ('shop_site', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop_site.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='bill',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='deliveries',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_site.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop_site.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='deliveries',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.store', verbose_name='Филиал'),
        ),
        migrations.AddField(
            model_name='bill',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cart.store', verbose_name='Филиал'),
        ),
    ]
