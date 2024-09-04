from app_menu.models import Menu


def get_menus(request):
    """Функция получает все меню из БД"""
    menus = Menu.objects.all()
    return {'menus': menus}
