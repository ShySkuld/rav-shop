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
        # 12 случайных товаров
        ids = Product.objects.values_list('id', flat=True)  # лист всех id
        random_id = random.sample(list(ids), 12)  # 12 уникальных id
        context['discount'] = Product.objects.filter(id__in=random_id)
        # все, кроме 12 случайных товаров
        context['not_discount'] = Product.objects.exclude(id__in=random_id)
        return context


class ProductInfoView(DetailView):
    model = Product
    template_name = 'item_card.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_object(self):
        # только опубликованные и в наличии
        return get_object_or_404(Product,
                                 slug=self.kwargs[self.slug_url_kwarg],
                                 is_published='PUB',
                                 stock_balance__gt=0)
