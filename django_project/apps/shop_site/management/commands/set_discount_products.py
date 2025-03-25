import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from apps.shop_site.models import Product

class Command(BaseCommand):
    help = 'Устанавливает на 12 случайных товаров скидку от 79% до 92%'

    def handle(self, *args, **kwargs):
        # лист всех id
        ids = Product.objects.values_list('id', flat=True)
        # 12 уникальных id
        random_id = random.sample(list(ids), 12)

        for product in Product.objects.filter(id__in=random_id):
            # актуальная текущая цена (из всех изменений цен, беру последний объект)
            pricechange_object = product.price.all().last()
            pricechange_object.discount_percent = random.randint(79,92)     # делаем скидку :)
            # перекидываю текущую цены в старую цену
            pricechange_object.old_price = pricechange_object.current_price
            # умножаем текущую цену на 15 и делим на 100,
            # чтобы заранее перевести скидку из процентов

            disc_koeff = Decimal('0.15')
            pricechange_object.current_price *= disc_koeff
            pricechange_object.current_price *= pricechange_object.discount_percent
            pricechange_object.is_discount = True
            pricechange_object.save()

        print(f'Установили скидку для товаров с id = {random_id}')


