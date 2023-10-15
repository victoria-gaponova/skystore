from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('country', 'inn', 'address')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('get_products_name', 'name', 'number', 'is_active')

    def get_products_name(self, obj):
        return '; '.join([product.name for product in obj.products.all()])