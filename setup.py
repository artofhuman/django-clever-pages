#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-clever-pages',
    version='0.2',
    description='App for create pages',
    author='Pupkov Semen',
    author_email='semen.pupvko@gmail.com',
    url='https://github.com/artofhuman/django-clever-pages',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-mptt>=0.6.0',
        'django-meta>=0.0.2',
        'feincms==1.7.7'
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
