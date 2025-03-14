import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from apps.shop_site.models import Product, PriceChange



class HomePageView(ListView):
    model = Product
    template_name = 'templates/home_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 12 товаров со скидкой
        context['discount'] = context['object_list'].filter(price__is_discount=True)[:12]

        # все, кроме скидочных товаров
        context['not_discount'] = context['object_list'].exclude(price__is_discount=True)

        return context


class ProductInfoView(DetailView):
    model = Product
    template_name = 'item_card.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        """ переопределяю для вывода только 4 фото для каждого товара """
        context = super().get_context_data(**kwargs)
        photos = kwargs['object'].photo_set.all()  # все фотки товара
        if photos.count() > 4:  # если их > 4, то беру первые 4
            photos = photos[:4]
        context['photos'] = photos  # 4 фотки
        # передаю товары аналогичной категории
        subcategory = kwargs['object'].subcategory
        current_product_id = kwargs['object'].id
        context['items_for_you'] = (Product.objects.
                                    filter(subcategory=subcategory).
                                    exclude(id=current_product_id))
        return context
