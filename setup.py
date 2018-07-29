from setuptools import setup, find_packages
import codecs
import os
import tushare

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_desc = """
TuShare
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
    
Upgrade
---------------

    pip install tushare --upgrade
    
Quick Start
--------------

::

    import tushare as ts
    
    ts.get_hist_data('600848')
    
return::

                open    high   close     low     volume    p_change  ma5 \
    
    date
    2012-01-11   6.880   7.380   7.060   6.880   14129.96     2.62   7.060
    2012-01-12   7.050   7.100   6.980   6.900    7895.19    -1.13   7.020
    2012-01-13   6.950   7.000   6.700   6.690    6611.87    -4.01   6.913
    2012-01-16   6.680   6.750   6.510   6.480    2941.63    -2.84   6.813
    2012-01-17   6.660   6.880   6.860   6.460    8642.57     5.38   6.822
    2012-01-18   7.000   7.300   6.890   6.880   13075.40     0.44   6.788
    2012-01-19   6.690   6.950   6.890   6.680    6117.32     0.00   6.770
    2012-01-20   6.870   7.080   7.010   6.870    6813.09     1.74   6.832
    
"""

def read_install_requires():
    with open('requirements.txt', 'r') as f:
        res = f.readlines()
    res = list(map(lambda s: s.replace('\n', ''), res))
    return res

setup(
    name='tushare',
    version=tushare.__version__,
    description='A utility for crawling historical and Real-time Quotes data of China stocks',
#     long_description=read("READM.rst"),
    long_description = long_desc,
    author='Jimmy Liu',
    author_email='jimmysoa@sina.cn',
    license='BSD',
    url='http://tushare.org',
    keywords='Global Financial Data',
    classifiers=['Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: BSD License'],
    packages=find_packages(),
    package_data={'': ['*.csv']},
)