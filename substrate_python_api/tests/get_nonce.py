from substrate_python_api.tests.config import async_call
import json
from substrate_python_api.utils.blake2 import get_blake2_256
import base58


address = b"5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
result = base58.b58decode(b'5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY')

balance = b'System AccountNonce' + result[1:33]
array = bytearray(result[1:33])
print(get_blake2_256(balance))

message = {"jsonrpc": "2.0",
           "method": "state_getStorage",
           "params": [get_blake2_256(balance)],
           "id": 1}


def deal_with_message(data):
    a = json.loads(data)['result']
    nonce = int.from_bytes(bytearray.fromhex(a[2:]), byteorder='little')
    print(nonce)


async_call("state_getStorage", [get_blake2_256(balance)], deal_with_message)
