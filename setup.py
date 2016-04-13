# -*- coding: utf-8 -*-

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


install_requires = [
    'selenium'

]

if py_version != (3, 2):
    # Babel not available on 3.2
    install_requires.append("Babel")
install_requires = [
    'selenium'
]

setup(
    name='test_livecount',
    version='0.1',
    description='',
    author='',
    author_email='',
    url='',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
)