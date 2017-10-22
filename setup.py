#!/usr/bin/env python3
from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path
import sys
import shutil
import os

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ly-bar-incr',
    version='0.4',

    description=('Increment bar numbers in comments and bar number checks of a'
                 ' lilypond file.'),
    long_description=long_description,
    url='https://github.com/rickh94/ly-bar-incr',

    author='Rick Henry',
    author_email='fredericmhenry@gmail.com',

    license='MIT',
    python_requires='>=2.7',
    install_requires=['click'],

    py_modules=['ly_bar_incr'],
    entry_points={
        'console_scripts': [
            'ly-bar-incr=ly_bar_incr:cli',
            ],
        },
    )
#
# # install man pages
# if 'install' in sys.argv:
#     man_path = '/usr/share/man/man1/'
# if os.path.exists(man_path):
#     print("Installing man pages")
#     man_page = "doc/ly-bar-incr.1.gz"
#     shutil.copy2(man_page, man_path)
#     os.chmod(man_path + 'ly-bar-incr.1.gz', int('444', 8))
