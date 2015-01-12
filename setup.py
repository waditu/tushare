from distutils.core import setup
import codecs
import os
import sys

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='tushare',
    version='0.1.2',
    description='TuShare is a utility for crawling historical data of China stocks',
#     long_description=read("README.md"),
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
