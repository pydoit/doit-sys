# -*- coding: utf-8 -*-

from setuptools import setup

setup (
    name = 'doit-sys',
    version = '0.1.dev0',
    author = 'Eduardo Naufel Schettino',
    author_email = 'schettino72@gmail.com',
    description = 'doit tasks for system stuff',
    url = 'https://github.com/schettino72/doit-sys/',
    keywords = ['doit',],
    platforms = ['any'],
    license = 'MIT',
    packages = ['doitsys'],
    install_requires = [
        'doit >= 0.25.0',
        'doit-cmd >=0.1, <0.2',
        ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
    ]
)
