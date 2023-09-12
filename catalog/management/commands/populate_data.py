import json

from catalog.models import Product, Category, Contact
from config.settings import BASE_DIR

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()
        with open(BASE_DIR / 'catalog/fixtures/category.json') as f:
            category_data = json.load(f)
            for category_item in category_data:
                Category.objects.create(
                    pk=category_item['pk'],
                    name=category_item['fields']['name'],
                    description=category_item['fields']['description']
                )
        with open(BASE_DIR / 'catalog/fixtures/product.json') as f:
            product_data = json.load(f)
            for product_item in product_data:
                category_pk = product_item['fields']['category']
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk=product_item['pk'],
                    name=product_item['fields']['name'],
                    description=product_item['fields']['description'],
                    image=product_item['fields']['image'],
                    category=category,
                    price=product_item['fields']['price'],
                    created_at=product_item['fields']['created_at'],
                    last_modified=product_item['fields']['last_modified']
                )
        with open(BASE_DIR / 'catalog/fixtures/contact.json') as f:
            contact_data = json.load(f)
            for contact_item in contact_data:
                Contact.objects.create(
                    pk=contact_item['pk'],
                    country=contact_item['fields']['country'],
                    inn=contact_item['fields']['inn'],
                    address=contact_item['fields']['address']
                )