from django.shortcuts import render

from goods.models import Categories, Product

def catalog(request):

    goods = Product.objects.all()


    context = {
        'title': 'Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')
