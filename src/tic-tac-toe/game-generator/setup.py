#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Set up to create the distribution package.
"""
from distutils.core import setup

from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize(
        'main.py',
        language_level='3',
    )
)
