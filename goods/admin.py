from django.contrib import admin
from goods.models import Categories, Product

@admin.register(Categories) #тонкая настройка отображения админки
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product) 
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}