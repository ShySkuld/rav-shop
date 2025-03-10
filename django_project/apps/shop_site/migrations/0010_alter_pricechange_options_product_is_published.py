# Generated by Django 5.1.4 on 2025-01-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0009_alter_pricechange_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricechange',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.CharField(choices=[('SOLD', 'Распродано'), ('PUB', 'Опубликован'), ('PW', 'Черновик')], default='PW', verbose_name='Статус'),
        ),
    ]
