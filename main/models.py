from django.db import models


# Create your models here.
class Product(models.Model):
    name_prod = models.CharField(max_length=100, verbose_name='Наименование')
    description_prod = models.CharField(max_length=100, verbose_name='Описание')
    img_prod = models.ImageField(upload_to='preview', verbose_name='Превью', null=True, blank=True)
    category_prod = models.CharField(max_length=100, verbose_name='Категория')
    price_prod = models.IntegerField(verbose_name='Цена', null=True, blank=True, help_text='Введите цену продукта в рублях')
    data_create_prod = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    data_change_prod = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name_prod} {self.category_prod} {price_prod}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name_prod = models.CharField(max_length=100, verbose_name='Наименование')
    category_prod = models.CharField(max_length=100, verbose_name='Категория')

    def __str__(self):
        return f'{self.name_prod} {self.category_prod}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'