# Django Clever Pages [![Tests](https://travis-ci.org/artofhuman/django-clever-pages.png)](https://travis-ci.org/artofhuman/django-clever-pages)

# RU

Простое приложение для организации статичных страниц.

* Умеет строить древовидную структуру страниц на основе mptt.
* Генерирует урл начиная от родительской страницы
* Имеет drag-n-drop управление страницами в админке
* Определены индексы для haystack, sphinx в планах
* Метатеги на основе django-meta

# EN

Simple application that allows you to organize pages in a tree

* Organize pages in tree structure
* Generate page url, include all parents
* Drag-n-dtop interface in admin
* Include Search indices for haystack. Sphinx in plans
* Include meta tags via djago-meta

## Instalation

Add to your `reqs.txt` file and make `pip install -r reqs.txt`

    pip install git+git://github.com/artofhuman/django-clever-pages

Add this line to your settings.py

~~~~ Python
    INSTALLED_APPS = (
        "page",
    )
~~~~

Add it to end urls.py
~~~~ Python
    urlpatterns = patterns('',
        ('', include('page.urls'))
    )
~~~~
You can define more templates in settings.py
~~~~ Python
    PAGE_TEMPLATES = (
        ('contacts', u'Contacts')
    )
~~~~

Meta tags in base.html
~~~~ Django
<head>
    {% if meta.title %}
        <title>{{ meta.title }}</title>
    {% else %}
        <title>{% block title %}{% endblock %}</title>
    {% endif %}
    {% if meta.description %}{% meta 'description' meta.description %}{% endif %}
    {% if meta.keywords %}{% meta_list 'keywords' meta.keywords %}{% endif %}
</head>
~~~~

# TODO
- Add test
- Add section about haystack
- Add sphinx integration
- Add dependences
- Add screenshot

P.S. Sorry for my bad english :)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/artofhuman/django-clever-pages/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

