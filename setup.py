#!/usr/bin/env python
# -*- coding: utf-8 -*-
from drf_scaffolding import __author__, __version__

from setuptools import find_packages, setup


setup(
    name='drfscaffolding',
    version=__version__,
    description=(
        'Django app which allow create full APIs based on your models defined '
        'in your project.'
    ),
    author=__author__,
    author_email='angel.david.lagunas@gmail.com',
    url='https://angellagunas.github.io/drf-scaffolding/',
    download_url=(
        'https://github.com/angellagunas/drf-scaffolding/archive/0.1.tar.gz'
    ),
    install_requires=[
        'soft_drf==0.3.13',
    ],
    packages=find_packages(),
    classifiers=[
        'Framework :: Django'
    ]
)
