from django.core.management.base import BaseCommand
from apps.shop_site.models import Product

class Command(BaseCommand):
    help = 'Возвращаю стоимость скидочных продуктов в начальное состояние'

    def handle(self, *args, **kwargs):
        discounted_products = Product.objects.filter(price__is_discount=True)
        for product in discounted_products:
            # актуальная текущая цена (из всех изменений цен, беру последний объект)
            pricechange_object = product.price.all().last()
            pricechange_object.discount_percent = 0

            pricechange_object.current_price = pricechange_object.old_price
            pricechange_object.old_price = 0
            pricechange_object.is_discount = False
            pricechange_object.save()
        print(f'Вернул стоимость для {len(discounted_products)} продуктов')

