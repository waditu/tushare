from distutils.core import setup

setup(
    name='tushare',
    version='0.1.0',
    description='TuShare is a utility for crawling historical data of China stocks',
    author='Jimmy Liu',
    author_email='jimmysoa@sina.cn',
    license='BSD',
    url='https://github.com/jimmysoa/tushare',
    keywords='china stock data',
    classifiers=['Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: BSD License'],
    packages=['tushare','tushare.stock'],
)
