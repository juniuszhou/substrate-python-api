from substrate_python_api.tests.config import async_call


message = {"jsonrpc": "2.0",
           "method": "state_getStorage",
           # key of storage.
           "params": ["0x3f54a7d3730b866b50e6c1d2817d9ead3bcb7a693d04c3be6712bde3f17facca"],
           "id": 1}


def deal_with_message(data):
    print(data)


async_call(message['method'], message['params'], deal_with_message)
