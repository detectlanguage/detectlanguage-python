import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('detectlanguage/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name = 'detectlanguage',
    packages = ['detectlanguage'],
    version = version,
    description = 'Language Detection API Client',
    author = 'Laurynas Butkus',
    author_email = 'info@detectlanguage.com',
    url = 'https://github.com/detectlanguage/detectlanguage-python',
    download_url = 'https://github.com/detectlanguage/detectlanguage-python',
    keywords = ['language', 'identification', 'detection', 'api', 'client'],
    install_requires= ['requests>=1.2.0'],
    classifiers = [],
    license = 'MIT',
)
