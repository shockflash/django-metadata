#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-metadata',
    version='1.1-beta',
    description='Django Metadata allows you to add more data than the default fields',
    author='Leander Hanwald',
    author_email='leander@hanwald.de',
    url='http://code.google.com/p/django-metadata/',
    packages=[
        'metadata',
    ],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)