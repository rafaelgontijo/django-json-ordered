# -*- coding: utf-8 -*-
#!/usr/bin/env python

from io import open

from setuptools import find_packages, setup

from django_json_ordered.meta import VERSION

setup(
    name='django-json-ordered',
    version=str(VERSION),
    description="It's an ordered json field",
    long_description=open('README.md', encoding='utf-8').read(),
    author='Shinneider Libanio da Silva',
    author_email='shinneider-libanio@hotmail.com',
    url='https://github.com/shinneider/django_admin_related',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)