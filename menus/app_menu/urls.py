from django.urls import path
from app_menu.views import home_view, menu_view


urlpatterns = [
    path('', home_view, name='index'),
    path('<path:path>/', menu_view, name='menu'),
]
