#!/usr/bin/env python
from os import path as op
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


install_requires = [
    'sanic >= 0.7.0',
    'raven',
    'raven-aiohttp'
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pylint',
    'pytest',
    'pytest-sugar',
    'pytest-sanic',
    'pytest-mock',
    'mock'
]

setup(
    name='sanic-sentry-error-handler',
    version='0.1.2',
    license='MIT',
    description='Sanic error handlert that integrates with Sentry',
    long_description=readme,
    platforms=('Any'),
    keywords=['sanic', 'sentry'],

    author='Eran Kampf',
    url='https://github.com/ekampf/sanic-sentry-error-handler',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=install_requires,
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
