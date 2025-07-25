#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
multitasking: Non-blocking Python methods using decorators
https://github.com/ranaroussi/multitasking
Copyright 2016-2021 Ran Aroussi
"""

import codecs
import os
from setuptools import setup, find_packages

# Get the long description from the README file
with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                              'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='multitasking',
    version='0.0.12',
    description='Non-blocking Python methods using decorators',
    long_description=long_description,
    url='https://github.com/ranaroussi/multitasking',
    author='Ran Aroussi',
    author_email='ran@aroussi.com',
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    platforms=['any'],
    keywords='multitasking multitask threading async',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    install_requires=[]
)
