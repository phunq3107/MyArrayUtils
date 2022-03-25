from setuptools import find_packages, setup

name = 'myarrayutils'
version = '0.0.1'
description = 'Myarrayutils is a collection of small Python functions which make working with an array easier'
author = ''
license = 'MIT'

setup(
    name=name,
    packages=find_packages(),
    version=version,
    description=description,
    author=author,
    license=license,
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
