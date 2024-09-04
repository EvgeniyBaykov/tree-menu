from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from app_menu.models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ['id', 'title']
    search_fields = ['title']
    inlines = [MenuItemInline, ]


@admin.register(MenuItem)
class MenuItemAdmin(DjangoMpttAdmin):
    pass
