from substrate_python_api.tests.config import async_call
import json

message = {"jsonrpc": "2.0", "method": "chain_getHeader", "params": [], "id": 1}


def deal_with_message(data):
    header = json.loads(data)
    block_number = int(header['result']['number'], 16)
    print(block_number)


async_call(message['method'], message['params'], deal_with_message)
