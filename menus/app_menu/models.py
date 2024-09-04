from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    """Класс описывающий меню"""
    title = models.CharField(max_length=255, db_index=True, unique=True, verbose_name=_('название меню'))
    description = models.CharField(max_length=1000, verbose_name=_('описание меню'))

    class Meta:
        verbose_name = _('Меню')
        verbose_name_plural = _('Меню')

    def __str__(self):
        return self.title


class MenuItem(MPTTModel):
    """Класс описывающий пункты меню"""
    name = models.CharField(max_length=200, verbose_name=_('название пункта меню'))
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='subitem',
                            verbose_name=_('родительский пункт'))
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, related_name='items', verbose_name=_('меню'))

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('пункт')
        verbose_name_plural = _('пункты')

    def __str__(self):
        return f'{self.menu.title} - {self.name}'
