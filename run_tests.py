from django.conf import settings
from django.core.management import call_command

def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'page',
        ),
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'testing.db'
            }
        }
    )

    # Fire off the tests
    call_command('test', 'page')

if __name__ == '__main__':
    main()
