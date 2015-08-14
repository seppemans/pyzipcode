from setuptools import setup, find_packages
import sys, os

version = '0.4.1'

try:
    import sqlite3
except ImportError:
    requires = ['pysqlite']
else:
    requires = []

setup(name='pyzipcode',
      version=version,
      description="query zip codes and location data",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='zip code distance',
      author='Nathan Van Gheem',
      author_email='vangheem@gmail.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      """,

      # Include additional files into the package
      include_package_data=True,
      package_data = {
          '': ['zipcodes.db'],
      }
      )
