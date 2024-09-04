from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка всех фикстур'

    def handle(self, *args, **options):
        management.call_command('loaddata', 'menus/app_menu/fixtures/menus.json')
        management.call_command('loaddata', 'menus/app_menu/fixtures/menuitems.json')
