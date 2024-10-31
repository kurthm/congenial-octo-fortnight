from setuptools import setup, find_packages

setup(
    name = 'fortnight', # name of the package
    version = '0.1.1',
    packages = 'fortnight', # could also do a list if you have a bunch # or find_packages() will find init.py modules and gets that package
    requires=['numpy <= 2.0', 'pandas']
    ) 