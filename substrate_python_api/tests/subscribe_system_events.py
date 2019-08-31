from substrate_python_api.tests.config import async_subscribe, backend_sub
import json
from substrate_python_api.utils.xxHash import get_xxhash_128
import time

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


events = b'System Events'

print(get_xxhash_128(events))
method = 'state_subscribeStorage'
params = [(get_xxhash_128(events),)]


t = backend_sub(method, params, callback, debug=False)

print('over')

time.sleep(10)

print('over again')

t.stop()



