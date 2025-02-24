from django.urls import path, include
from . import views
from .views import HomePageView, ProductInfoView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('product/<str:product_subcategory>/<slug:product_slug>/',
         ProductInfoView.as_view(),
         name='product'),
]