# -*- coding: utf-8 -*-
import sys
from setuptools import setup

# validation
if sys.version_info < (3, 4):
    print("Running chainer-dashboard requires at least Python 3.4 to run.")
    sys.exit(1)

setup(
    name='chainer-dashboard',
    version='0.0.1',
    packages=['DashBoard'],
    install_requires=['flask','matplotlib','pandas','seaborn'],
    scripts=['bin/runserver'],
    url='https://github.com/butsugiri/chainer-dashboard',
    zip_safe=False,
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.4',
    ],
)
