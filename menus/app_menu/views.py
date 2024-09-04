from django.shortcuts import render


def home_view(request, *args, **kwargs):
    """Главная страница с меню"""
    return render(request, 'app_menu/index.html')


def menu_view(request, *args, **kwargs):
    """Страница с развернутым меню"""
    path_lst = kwargs['path'].split('/')
    m_name = path_lst[0]
    i_name = path_lst[1] if len(path_lst) > 1 else None
    context = {
        'm_name': m_name,
        'i_name': i_name
    }
    return render(request, 'app_menu/index.html', context=context)
