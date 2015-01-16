from distutils.core import setup
import codecs
import os

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_desc = """
tushare
===============

.. image:: https://api.travis-ci.org/waditu/tushare.png?branch=master
    :target: https://travis-ci.org/waditu/tushare

.. image:: https://badge.fury.io/py/tushare.png
    :target: http://badge.fury.io/py/tushare

* easy to use as most of the data returned are pandas DataFrame objects
* can be easily saved as csv, excel or json files
* can be inserted into MySQL or Mongodb

Target Users
--------------

* financial market analyst of China
* learners of financial data analysis with pandas/NumPy
* people who are interested in China financial data

Installation
--------------

    pip install tushare
"""


setup(
    name='tushare',
    version='0.1.4',
    description='TuShare is a utility for crawling historical and Realtime Quotes data of China stocks',
#     long_description=read("READM.rst"),
    long_description = long_desc,
    author='Jimmy Liu',
    author_email='jimmysoa@sina.cn',
    license='BSD',
    url='https://github.com/waditu/tushare',
    keywords='china stock data',
    classifiers=['Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: BSD License'],
    packages=['tushare','tushare.stock'],
)