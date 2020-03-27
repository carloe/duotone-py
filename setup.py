# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='duotone',
    version='0.1',
    description='Apply duotone effect to images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/carloe/dutone',
    author='Carlo Eugster',
    author_email='carlo@relaun.ch',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'Pillow',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'duotone=duotone.__main__:cli',
        ],
    },
)
