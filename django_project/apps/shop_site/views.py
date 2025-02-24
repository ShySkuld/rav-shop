import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from apps.shop_site.models import Product



class HomePageView(ListView):
    model = Product
    template_name = 'templates/home_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # 12 случайных товаров
        # context['object_list'] = Product.objects.all()
        ids = context['object_list'].values_list('id', flat=True)  # лист всех id
        random_id = random.sample(list(ids), 12)  # 12 уникальных id
        context['discount'] = context['object_list'].filter(id__in=random_id)
        # все, кроме 12 случайных товаров
        context['not_discount'] = context['object_list'].exclude(id__in=random_id)
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
