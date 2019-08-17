from substrate_python_api.tests.config import async_call


message = {"jsonrpc": "2.0",
           "method": "state_getStorage",
           # key of storage.
           "params": ["0xb87be889f43fdcf49af3d74b74646da1905a4e53f0ceb97476a6539bfe60d588"],
           "id": 1}


def deal_with_message(data):
    print(data)


async_call(message['method'], message['params'], deal_with_message)
