Setup
======
Установка через pip
pip install git+git://github.com/artofhuman/django-clever-pages

    INSTALLED_APPS = (
        "page",
    )

urls.py:

Добавляем в самый конец правила

    urlpatterns = patterns('',
        ...
        url(r'^ajax_block/', include('ajax_block.urls')),

    )

Определение шаблонов
в settings.py

    PAGE_TEMPLATES = (
        ('contacts', u'Контакты')
    )
