from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length = 255, unique = True, verbose_name = 'Название')
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255, unique = True, verbose_name = 'Название')
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')
    description = models.TextField(blank = True, null = True, verbose_name = 'Описание')
    image = models.ImageField(upload_to='goods_images', blank = True, null = True, verbose_name= 'Изображения')
    price = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 2, verbose_name = 'Цена')
    length = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 0, verbose_name = 'Длина')
    width = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 0, verbose_name = 'Ширина')
    height = models.DecimalField(default = 0.00, max_digits = 7, decimal_places = 0, verbose_name = 'Высота')
    category = models.ForeignKey(to=Categories, on_delete = models.CASCADE, verbose_name = 'Категория')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self) -> str:
        return self.name
    
    def display_id(self):
        return f"{self.id:05}" #пять нулей перед числом
