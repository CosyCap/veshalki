from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Имя')
    phone_number = models.CharField(max_length = 15, verbose_name = 'Номер телефона')
    email = models.EmailField(max_length = 50, verbose_name = 'Адрес email')
    question = models.TextField(null = True, verbose_name = 'Заявка')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"Заявка от {self.name}, {self.phone_number}"