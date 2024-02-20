from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('vse-tovary/', views.catalog, {'category_slug': 'vse-tovary'}, name='vse_tovary'),  # Добавляем новый URL-шаблон
    path('product/<slug:product_slug>/', views.product, name='product'),
]
