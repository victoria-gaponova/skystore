import json
from config.settings import BASE_DIR

from django.core.management.base import BaseCommand
from catalog.models import Product, Contact, Category, Version


class Command(BaseCommand):
    help = 'Заполнение базы данных данными из нескольких файлов'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Contact.objects.all().delete()
        Category.objects.all().delete()
        Version.objects.all().delete()

        try:
            with open(BASE_DIR / 'catalog/fixtures/categories.json', 'r', encoding='cp1251') as file:
                category_data = json.load(file)
                for item in category_data:
                    Category.objects.create(
                        pk=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description']
                    )
            with open(BASE_DIR / 'catalog/fixtures/products.json', 'r', encoding='cp1251') as file:
                product_data = json.load(file)
                for item in product_data:
                    category_pk = item['fields']['category']
                    category = Category.objects.get(pk=category_pk)
                    Product.objects.create(
                        pk=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description'],
                        image=item['fields']['image'],
                        category=category,
                        price=item['fields']['price'],
                        created_at=item['fields']['created_at'],
                        last_modified=item['fields']['last_modified']
                    )

            with open(BASE_DIR / 'catalog/fixtures/contacts.json', 'r', encoding='cp1251') as file:
                contact_data = json.load(file)
                for item in contact_data:
                    Contact.objects.create(
                        pk=item['pk'],
                        country=item['fields']['country'],
                        inn=item['fields']['inn'],
                        address=item['fields']['address']
                    )
            with open(BASE_DIR / 'catalog/fixtures/version.json', 'r', encoding='cp1251') as file:
                version_data = json.load(file)
                for item in version_data:
                    version = Version.objects.create(
                        number=item['fields']['number'],
                        name=item['fields']['name'],
                        is_active=item['fields']['is_active']
                    )
                    version.products.set(item['fields']['products'])

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

        else:
            self.stdout.write(self.style.SUCCESS('Данные успешно добавлены в базу данных'))
