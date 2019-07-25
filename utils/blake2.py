from pyblake2 import *

blake_hash = blake2b(digest_size=20)
blake_hash.update(b'Take that, Keccak')
print(blake_hash.digest())

