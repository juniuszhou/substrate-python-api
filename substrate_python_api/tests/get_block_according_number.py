from substrate_python_api.tests.config import async_call
import json

block_number = 1897
message = {"jsonrpc": "2.0", "method": "chain_getBlockHash",
           "params": [block_number], "id": 1}


class Data:
    block_hash = None


def get_hash(data):
    header = json.loads(data)
    Data.block_hash = header['result']
    print(Data.block_hash)


async_call(message['method'], message['params'], get_hash)

message = {"jsonrpc": "2.0", "method": "chain_getBlock", "params": [], "id": 2}


def get_block(data):
    header = json.loads(data)
    Data.block_hash = header['result']
    log = header['result']['block']['header']['digest']['logs']
    print(log)


async_call(message['method'], [Data.block_hash], get_block)



