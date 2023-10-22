#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pak',
    version='0.1.0',
    description='An umka package manager',
    long_description=readme,
    author='Marek Maškarinec',
    author_email='marek@mrms.cz',
    url='https://git.sr.ht/~mrms/pak',
    license=license,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pak = pak:main'
        ]
    }
)
