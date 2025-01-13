# Generated by Django 5.1.4 on 2025-01-13 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adv',
            options={'verbose_name': 'Рекламное объявление', 'verbose_name_plural': 'Рекламные объявления'},
        ),
        migrations.AlterModelOptions(
            name='advtype',
            options={'verbose_name': 'Категорию рекламы', 'verbose_name_plural': 'Категории рекламы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'Фирму-производитель', 'verbose_name_plural': 'Фирмы-производители'},
        ),
        migrations.AlterModelOptions(
            name='manufacturercountry',
            options={'ordering': ('name',), 'verbose_name': 'Странa-изготовитель', 'verbose_name_plural': 'Страны-изготовители'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотографию', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='pricechange',
            options={'verbose_name': 'Историю изменения цены', 'verbose_name_plural': 'Истории изменения цен'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='manufacturer',
            name='country',
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop_site.manufacturercountry', verbose_name='Страна-изготовитель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.manufacturer', verbose_name='Фирма-производитель'),
        ),
    ]