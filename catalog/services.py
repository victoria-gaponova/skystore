from django.core.cache import cache

from catalog.models import Category


def get_categories():
    # Пробуем получить данные из кеша
    categories = cache.get('categories')

    # Если данные не найдены в кеше, выполнить их выборку из базы даннных
    if categories is None:
        categories = Category.objects.all()

        # Сохраним результаты выборки в кеше на определенное время
        cache.set('categories', categories, 3600)
    return categories
