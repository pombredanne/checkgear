#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
 
setup(
        name             = 'checkgear',
        version          = '0.0.1',
        description      = 'Library Vulnerability Checker from CVE.',
        long_description = '[command]$checkgear',
        classifiers      = [
                           'Topic :: Security',
                           ],
        license          = 'MIT',
        author           = 'Sou Komatsu',
        author_email     = 'sou.komatsu@gmail.com',
        url              = 'https://github.com/sou-komatsu/checkgear',
        keywords         = ['python','security','cve'],
        packages         = find_packages(),
        install_requires = [],
        entry_points ="""
            [console_scripts]
            checkgear = checkgear:main
        """,
     )
