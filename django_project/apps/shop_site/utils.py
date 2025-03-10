#  https://django.fun/qa/353351/
import random
from decimal import Decimal

from PIL import Image

def resize_image_to_square(image) -> None:
    # image - поле photo объекта класса Photo
    img = Image.open(image.path)

    # Проверяет имеет изображение прозрачный фон или нет для установки маски
    # маска поставит белый фон для отсутствующего фона
    mask = None
    if (img.mode in ('RGBA', 'LA') or
            (img.mode == 'P' and 'transparency' in img.info)):
        mask = img

    # проверяю, что длиннее у картинки - ширина или длина и добавляю белые
    # полоски по краям. В итоге получаю квадратное изображение.
    if img.width > img.height:
        size_diff = img.width - img.height
        background = Image.new('RGB',
                               (img.size[0], img.size[1] + size_diff),
                               (255, 255, 255))
        background.paste(img, (0, size_diff // 2), mask=mask)
    else:
        size_diff = img.height - img.width
        background = Image.new('RGB',
                               (img.size[0] + size_diff, img.size[1]),
                               (255, 255, 255))
        background.paste(img,  (size_diff // 2, 0), mask=mask)

    background.save(image.path)


def set_discount_price(queryset):
    for product in queryset:
        # актуальная текущая цена (из всех изменений цен, беру последний объект)
        pricechange_object = product.price.all().last()
        pricechange_object.discount_percent = random.randint(79, 92) # делаем скидку :)
        # умножаем текущую цену на 15 и делим на 100,
        # чтобы заранее перевести скидку из процентов

        disc_koeff = Decimal("0.15")
        pricechange_object.current_price *= disc_koeff
        pricechange_object.current_price *= pricechange_object.discount_percent
        pricechange_object.is_discount = True
        pricechange_object.save()

