import schnorrpy
import binascii
import base64
import os


class KeyPair:
    def __init__(self, _public_key, _private_key):
        assert (len(_public_key) == 32)
        assert (len(_private_key) == 64)
        print('init is ok.')
        self.private_key = _private_key
        self.public_key = _public_key


class Sr25519:
    def __init__(self):
        pass

    # generate key pair from 32 bytes seed.
    @staticmethod
    def generate_key_pair_from_seed(seed=None):

        if seed is None:
            seed = os.urandom(32)

        key_pair = schnorrpy.keypair_from_seed(seed)
        return KeyPair(key_pair[0], key_pair[1])


Sr25519.generate_key_pair_from_seed()
