#  https://django.fun/qa/353351/
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
