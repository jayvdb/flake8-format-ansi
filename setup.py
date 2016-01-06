# -*- coding: utf-8 -*-
from setuptools import setup

name = 'flake8-format-ansi'
module_name = name.replace('-', '_')
init_py = open(module_name + '.py').read().splitlines()
metadata = [('__doc__', line) if line.startswith('"""')
            else line.split(' = ')
            for line in init_py
            if line.startswith('__') or line.startswith('"""')]
metadata = dict((name[2:-2], value.strip('"\'')) for name, value in metadata)


setup(
    name=name,
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    description=metadata['doc'],
    url=metadata['url'],
    license=metadata['license'],
    keywords='flake8 color ansi error format',
    install_requires=['flake8', 'pep8>=1.3'],
    py_modules=[module_name],
    entry_points={
        'flake8.extension': [
            '%s = %s:%s' % (name, module_name, 'ANSIFormatExtension'),
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
