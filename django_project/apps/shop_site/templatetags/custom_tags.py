from . import custom_filters
from django import template


register = template.Library()


# @register.simple_tag
# def custom_tag_percent():
#     """Умножает два числа."""
#     return custom_filters.koeff

# @register.inclusion_tag('result.html')
# def show_result(value):
#     """Отображает результат в отдельном шаблоне."""
#     return {'value': value}