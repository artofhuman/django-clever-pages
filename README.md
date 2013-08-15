# Django Clever Pages

Simple application that allows you to organize pages in a tree

## Instalation

Add to your `reqs.txt` file and make `pip install -r reqs.txt`

    pip install git+git://github.com/artofhuman/django-clever-pages

Add this line to your settings.py

    INSTALLED_APPS = (
        "page",
    )


Add it to end urls.py

    urlpatterns = patterns('',
        ('', include('page.urls'))
    )

You can define more templates in settings.py
        
    PAGE_TEMPLATES = (
        ('contacts', u'Contacts')
    )

# TODO

- Add more description in readme
- Add test
- Add section about haystack
- Add sphinx integration
- Add dependences
- Add screenshot

P.S. Sorry for my bad english :)
