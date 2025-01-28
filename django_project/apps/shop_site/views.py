import random
from django.shortcuts import render
from django.views.generic import ListView
from apps.shop_site.models import Product


# def index(request):
#     return render(request, 'templates/home_page.html')

class HomePageView(ListView):
    model = Product
    template_name = 'templates/home_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 12 случайных товаров
        ids = Product.objects.values_list('id', flat=True)  # лист всех id
        random_id = random.sample(list(ids), 12)  # 12 уникальных id
        context['ids'] = random_id
        context['discount'] = Product.objects.filter(id__in=random_id)
        return context