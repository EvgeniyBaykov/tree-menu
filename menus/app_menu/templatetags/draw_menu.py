from django import template
from django.core.exceptions import ObjectDoesNotExist

from app_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('app_menu/menu.html')
def draw_menu(m_name: str = None, i_name: str = None) -> dict:
    def get_menu(item_name: str = None, submenu: list = None):
        menu = list(all_items.filter(parent=None)) if item_name is None else list(
            all_items.filter(parent__name=item_name))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(all_items.get(name=item_name).parent.name, menu)
        except AttributeError:
            return get_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    all_items = MenuItem.objects.select_related('parent', 'menu').filter(menu__title=m_name).all()

    items = get_menu(i_name)
    return {'items': items, 'm_name': m_name}
