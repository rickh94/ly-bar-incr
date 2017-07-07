#!/usr/bin/env python3
from setuptools import setup,find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='ly_bar_incr',
    version='0.1',

    description='Increment bar numbers in comments and bar number checks of a lilypond file.',
    long_description=long_description,
    url='https://github.com/rickh94/ly-bar-incr',
    
    author='Rick Henry',
    author_email='fredericmhenry@gmail.com',

    license='GPLv3',
    python_requires='>=3',

    # install_requires=['sys','shutil','re','argparse'],

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ly_bar_incr=ly_bar_incr:main',
            ],
        },
    )
