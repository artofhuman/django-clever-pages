#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-clever-pages',
    version='0.1',
    description='App for create pages',
    author='Pupkov Semen',
    author_email='semen.pupvko@gmail.com',
    url='https://github.com/artofhuman/django-clever-pages',
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
