#!/usr/bin/env python

from setuptools import setup
import os
import re

setup(name='socrates_api',
      version='1.0.1',
      license='Apache Software License',
      description='Source of Truth for hardware, virtual machines, and networks',
      author='Klarna Bank AB',
      author_email='daniel.zakrisson@klarna.com',
      url='https://github.com/dhozac/socrates_api',
      packages=['socrates_api', 'socrates_api.migrations', 'socrates_api.templatetags'],
      install_requires=[
          'Django>=1.11,<2.0',
          'rethinkdb',
          'celery',
          'djangorestframework',
          'gevent>1.0.0',
          'requests',
          'pyghmi',
          'jsonpath_rw_ext',
          'netaddr',
          'deepdiff>3.2.0',
          'django_rethink',
      ],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: 7 - Inactive',
          'Environment :: Web Environment',
          'Framework :: Django :: 1.11',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Apache Software License',
          'Topic :: System :: Installation/Setup',
      ],
     )
