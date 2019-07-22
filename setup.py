#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: junius
# Mail: junius.zhou@gmail.com
# Created Time:  2019-07-20 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name="substrate-python-api",
    version="0.0.1",
    keywords=("pip", "substrate", "api"),
    description="python api for substrate",
    long_description="python api for substrate",
    license="MIT Licence",

    url="https://github.com/juniuszhou/substrate-pyton-api",
    author="junius",
    author_email="junius.zhou@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)

