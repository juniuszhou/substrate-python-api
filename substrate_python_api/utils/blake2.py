from pyblake2 import *


def get_blake2_256(data):
    # for substrate we must use blake 2b with 32 bytes setting.
    blake_hash = blake2b(digest_size=32)
    blake_hash.update(data)
    digest = blake_hash.digest()
    # print('blake digest raw is {}'.format([x for x in digest]))
    return '0x' + digest.hex()


def test():
    print(get_blake2_256(b'abc'))


