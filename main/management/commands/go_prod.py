from django.core.management import BaseCommand

from main.models import Product


class Command(BaseCommand):
    help = 'команда, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных'

    def handle(self, *args, **options):
        """фнкция очистки таблицы категории-Product БД и заполнение новыми данными"""
        Product.objects.all().delete()  # очистка таблицы Category

        # Добавить новые данные в базу данных
        new_items = [
            {'name_prod': 'Соки',
             'description_prod': 'Соки вкусные ',
             'img_prod': '',
             'category_prod': 'фрукты',
             'price_prod': '100'
             },
            # Добавьте здесь остальные данные, которые добавляем, здесь можно реалисовать распаковку из файла
        ]

        prod_list = []
        for item_data in new_items:
            prod_list.append(Product(**item_data))

        Product.objects.bulk_create(prod_list)  # заполняем БД