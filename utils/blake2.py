from pyblake2 import *


def get_blake2_256(data):
    # for substrate we must use blake 2b with 32 bytes setting.
    blake_hash = blake2b(digest_size=32)
    blake_hash.update(data)
    return '0x' + blake_hash.digest().hex()


def test():
    print(get_blake2_256(b'abc'))  # 0xba80a53f981c4d0d


test()

