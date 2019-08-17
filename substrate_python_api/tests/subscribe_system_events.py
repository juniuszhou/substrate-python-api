
from substrate_python_api.tests.config import async_subscribe
import json
from substrate_python_api.utils.blake2 import get_blake2_256
from substrate_python_api.utils.xxHash import get_xxhash_128
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
        print(data)
        Keep.skip_first = True


balance = b'System EventCount'

print(get_xxhash_128(balance))
method = 'state_subscribeStorage'
params = [(get_blake2_256(balance),)]


async_subscribe(method, params, callback)


