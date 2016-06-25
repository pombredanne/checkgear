#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from checkgear import __author__, __version__, __license__
 
setup(
        name             = 'checkgear',
        version          = __version__,
        description      = 'Library Vulnerability Checker from CVE.',
        license          = __license__,
        author           = __author__,
        author_email     = 'sou.komatsu@gmail.com',
        url              = 'https://github.com/sou-komatsu/checkgear',
        keywords         = 'python',
        packages         = find_packages(),
        install_requires = [],
     )
