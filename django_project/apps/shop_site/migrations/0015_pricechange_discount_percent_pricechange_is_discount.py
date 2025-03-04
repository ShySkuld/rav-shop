# Generated by Django 5.1.6 on 2025-03-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0014_remove_product_name_product_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricechange',
            name='discount_percent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pricechange',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
    ]
