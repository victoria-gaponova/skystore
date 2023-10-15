from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создание суперюзера'

    def handle(self, *args, **options):
        user = User.objects.create(
            email='victoria.gaponava@gmail.com',
            first_name='Admin',
            last_name='Skypro',
            is_staff=True,
            is_superuser=True,
            is_verified_email=True
        )
        user.set_password('adm11111')
        user.save()
