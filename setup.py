# setup.py
from setuptools import setup, find_packages

setup(
    name='MockUnit',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 這裡可以列出你的依賴項目，例如 'requests', 'pytest' 等
    ],
    include_package_data=True,
    description='A Python project for mocking unit tests',
)
