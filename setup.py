#!/usr/bin/env python

from setuptools.depends import get_module_constant
from setuptools import setup

setup(
    name = 'detectlanguage',
    packages = ['detectlanguage'],
    version = get_module_constant('detectlanguage', '__version__'),
    description = 'Language Detection API Client',
    author = 'Laurynas Butkus',
    author_email = 'info@detectlanguage.com',
    url = 'https://github.com/detectlanguage/detectlanguage-python',
    download_url = 'https://github.com/detectlanguage/detectlanguage-python',
    keywords = ['language', 'identification', 'detection', 'api', 'client'],
    install_requires= ['requests>=2.4.2'],
    classifiers = [],
    license = 'MIT',
)
