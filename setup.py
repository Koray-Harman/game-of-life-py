# -*- coding: utf-8 -*-

# Learn more: https://github.com/Koray-Harman/game-of-life-py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gameoflife',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Koray Harman',
    author_email='Koray-Harman@users.noreply.github.com',
    url='https://github.com/Koray-Harman/game-of-life-py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

