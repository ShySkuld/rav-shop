#  https://django.fun/qa/353351/
import random

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

        last_element = product.price.all().last() # последняя текущая цена
        last_element.old_price = last_element.current_price
        last_element.current_price *= 15 # умножаем на 15
        last_element.is_discount = True
        last_element.discount_percent = random.randint(79, 92) # делаем скидку :)
        last_element.save()

