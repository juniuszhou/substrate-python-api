from substrate_python_api.tests.config import async_call
from substrate_python_api.utils.xxHash import get_xxhash_128
import json


class Keep:
    hash_list = list()


def get_hash(data):
    json_data = json.loads(data)
    Keep.hash_list.append(json_data['result'])


for block_num in range(33110, 33111):
    async_call("chain_getBlockHash", [block_num], get_hash)


[print(x) for x in Keep.hash_list]


def get_storage(data):
    print(data)


storage = 'System EventCount'
for block_hash in Keep.hash_list[0:1]:
    print('============== block hash is {} '.format(block_hash))
    async_call("state_queryStorage", [[get_xxhash_128(storage), ], block_hash], get_storage, True)



