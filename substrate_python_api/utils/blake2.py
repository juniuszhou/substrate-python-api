from pyblake2 import *


def get_blake2_256(data):
    # for substrate we must use blake 2b with 32 bytes setting.
    blake_hash = blake2b(digest_size=32)
    blake_hash.update(data)
    digest = blake_hash.digest()
    # print('blake digest raw is {}'.format([x for x in digest]))
    return '0x' + digest.hex()


def test():
    key = b'LitentryStorage IdentitiesOwner'
    params = '0x672576b52b8b52d2d8a9e6aafa06654d269b1f98b2598d7f3e6bc98fdd3790c7'
    param_bytes = bytearray.fromhex(params[2:])
    print(get_blake2_256(key + param_bytes))

    key = b'LitentryStorage IdentitiesArray'
    params = 1
    param_bytes = bytearray.fromhex(params[2:])
    print(get_blake2_256(key + param_bytes))

# test()