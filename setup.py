# __author__ = 'daixinyu'
# coding=utf8
from setuptools import setup, find_packages
from com.version import version

setup(
    name="py_rpm",
    version=version,
    description="rpm testing",
    long_description=open("README.md").read(),
    packages=find_packages(),
    author="ShopEx",
    author_email="daixinyu@shopex.cn",
    license="LGPL",
    platforms=["README.md"],
)