#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='drfscaffolding',
    version='0.0.1',
    description=(
        'Aplicación Django que te permite crear APIs completas basándose en '
        'la definición de los modelos que tengas en tu proyecto'
    ),
    author='al',
    author_email='angel.david.lagunas@gmail.com',
    url='https://github.com/angellagunas/drf-scaffolding',
    download_url=(
        'https://github.com/angellagunas/drf-scaffolding/archive/0.1.tar.gz'
    ),
    install_requires=[
        'Django>=1.9',
        'djangorestframework',
        'django-rest-framework-nested',
        'django-rest-swagger'
    ],
    packages=find_packages(),
    classifiers=[
        'Framework :: Django'
    ]
)
