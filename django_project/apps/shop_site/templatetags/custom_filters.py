import random
from decimal import ROUND_DOWN

from django import template


register = template.Library()


@register.filter
def multiply(value, k):
    """Умножает значение на число"""
    a = value.to_integral_value(rounding=ROUND_DOWN) * (k // 100)
    print(a)
    return a
    # try:
    #     return int(value) * (int(k) // 100)
    # except (TypeError, ValueError):
    #     return value


@register.filter
def percent(value):
    """Возвращает процент скидки"""
    try:
        koeff = random.randrange(75, 91)
        return int(int(value) * 100 / (100 - koeff))
    except (TypeError, ValueError):
        return value



