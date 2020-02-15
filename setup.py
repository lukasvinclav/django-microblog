#!/usr/bin/env python

from setuptools import setup


setup(
    name='django-microblog',
    version='0.1.0',
    description='Simple blogging application for Django',
    short_description='Simple blogging application for Django',
    long_description=open('README.md').read(),
    packages=[
        'microblog',
        'microblog.migrations',
    ],
    include_package_data=True,
    install_requires=(
        'django',
        'Pillow'
    ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
    ],
    keywords='django blog post category'
)
