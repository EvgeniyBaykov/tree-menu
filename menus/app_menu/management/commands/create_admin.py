from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    _class = User
    help = 'Создание суперпользователя'

    def handle(self, *args, **kwargs):
        self._class.objects.create_superuser('admin', '', 'admin')
