# Generated by Django 5.1.4 on 2025-01-15 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0004_remove_product_category_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_site.subcategory', verbose_name='Подкатегория'),
        ),
    ]