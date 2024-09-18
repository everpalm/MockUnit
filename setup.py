# setup.py
from setuptools import setup, find_packages

setup(
    name='MockUnit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       'pytest', 'pytest-mock', 'pytest-repeat', 'pytest-testmon',
       'pytest-json-report', 'pytest-rerunfailures', 'pytest-dependency',
       'requests', 'pytest-cov'
    ],
    include_package_data=True,
    description='A Python project for mocking unit tests',
)
