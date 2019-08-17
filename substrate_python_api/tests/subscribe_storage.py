
from substrate_python_api.tests.config import async_subscribe
import json
from substrate_python_api.utils.blake2 import get_blake2_256
import base58


class Keep:
    skip_first = False


def callback(data):
    if Keep.skip_first:
        print(data)
        json_data = json.loads(data)
        print('block hash is {}'.format(json_data['params']['result']['block']))
        print(json_data['params']['result']['changes'])
    else:
        Keep.skip_first = True


address = b"5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
result = base58.b58decode(b'5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY')

balance = b'System AccountNonce' + result[1:33]
array = bytearray(result[1:33])
print(get_blake2_256(balance))
method = 'state_subscribeStorage'
params = [(get_blake2_256(balance),)]


async_subscribe(method, params, callback)


