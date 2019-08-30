import json
from substrate_python_api.utils.blake2 import get_blake2_256
from substrate_python_api.tests.config import async_call
from substrate_python_api.utils.codec import address_to_public_key


address = b"5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
balance = b'Balances FreeBalance' + address_to_public_key(address)


def deal_with_message(data):
    a = json.loads(data)['result']
    print(a[2:])
    print([print(x) for x in bytearray.fromhex(a[2:])])
    print(int.from_bytes(bytearray.fromhex(a[2:]), byteorder='little'))


async_call("state_getStorage", [get_blake2_256(balance)], deal_with_message)
