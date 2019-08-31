# substrate-python-api

This library provides a Python wrapper around all the methods exposed by a Subtrate network client.

## Python Version
All code well tested on Python 3.x version, Python 2.x not supported.

## Overview 

## Installation
1. install via pip
pip install subtrate-python-api
2. install from code
git clone https://github.com/juniuszhou/subtrate-python-api
python install setup.py

## Document
https://github.com/juniuszhou/substrate-python-api/wiki

## Example
from substrate_python_api.client.client import WSClient
client = WSClient(uri='ws://192.168.2.158:9944')
print(client.system_version())

## Contacts
junius.zhou@gmail.com

## Contributing





