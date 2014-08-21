#!/usr/bin/env python
import io
import sys
from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='django-clever-pages',
    version='0.3.1',
    description='App for create pages',
    long_description=io.open('README.md', encoding='utf-8').read(),
    author='Pupkov Semyon',
    author_email='semen.pupkov@gmail.com',
    url='https://github.com/artofhuman/django-clever-pages',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-mptt>=0.6.0',
        'django-meta>=0.0.3',
        'feincms==1.9.3'
    ],
    packages=find_packages(),
    package_data={
        'page': [
            'locale/*/*/*.*',
        ],
    },
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python 2.7',
        'Programming Language :: Python :: 3',
    )
)
