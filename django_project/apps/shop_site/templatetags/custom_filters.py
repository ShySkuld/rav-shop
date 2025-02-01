import random

from django import template


register = template.Library()


@register.filter
def multiply(value, k):
    """Умножает значение на число"""
    try:
        return int(int(value) * k)
    except (TypeError, ValueError):
        return value


@register.filter
def percent(value):
    """Возвращает процент скидки"""
    try:
        koeff = random.randrange(75, 91)
        return int(int(value) * 100 / (100 - koeff))
    except (TypeError, ValueError):
        return value


@register.filter
def random_percent(value):
    """Муляж скидки, возвращает случайное число процента скидки"""
    return random.randrange(75, 91)

