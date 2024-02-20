from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.core.paginator import Paginator
from goods.models import Product

def catalog(request, category_slug, page = 1):
    if category_slug == 'vse-tovary':
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(goods, 4) #Количество товаров на страницу 
    current_page = paginator.page(page)

    context = {
        'title': 'Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product 
    }

    return render(request, 'goods/product.html', context=context)