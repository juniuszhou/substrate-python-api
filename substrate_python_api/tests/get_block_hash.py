from substrate_python_api.tests.config import async_call
import json

message = {"jsonrpc": "2.0", "method": "chain_getBlockHash", "params": [1897], "id": 1}


def deal_with_message(data):
    header = json.loads(data)
    block_hash = header['result']
    print(block_hash)


async_call(message['method'], message['params'], deal_with_message)
