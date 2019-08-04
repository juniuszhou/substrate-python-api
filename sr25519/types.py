import base58
import codecs


class Address:
    pass


class PublicKey:
    def __init__(self, bytes_value):
        if len(bytes_value) != 32:
            raise Exception('wrong length of public key')
        self.bytes_value = bytes_value

    def to_hex(self):
        return self.bytes_value.hex()


class PrivateKey:
    def __init__(self, bytes_value):
        if len(bytes_value) != 32:
            raise Exception('wrong length of private key')
        self.bytes_value = bytes_value

    def to_hex(self):
        return self.bytes_value.hex()


class Signature:
    pass


def test_base58():
    test_str = "1234"
    print(base58.b58encode(test_str))

    public_key = "fc6c6696498ebf3df05cce70f2b66bca260603d25db68bccc08e11b69d76d012"
    print(codecs.decode(public_key, 'hex'))

    print(b'*' + codecs.decode(public_key, 'hex') + b'>\xa5')

    print(base58.b58encode(b'*' + codecs.decode(public_key, 'hex') + b'>\xa5'))
    print(base58.b58decode(b'5Hmg8FcLs8BntiybzUqhggd2B6JLF7BbXQsHMvxv8RroRXS4'))


def public_to_address(public_key):
    if public_key[0:2] == "0x":
        public_key = public_key[2:]
    return base58.b58encode(b'*' + codecs.decode(public_key, 'hex') + b'>\xa5')

# nani-3:substrate junius$ target/release/subkey generate
# Secret phrase `twenty warrior visit sword rose rely peace cash absent safe roof budget` is account:
#   Secret seed: 0xf524574cf9425c882105e2c04f9ba7c24d4527b1dec8f2a689f276d7c56cecc6
#   Public key (hex): 0xfc6c6696498ebf3df05cce70f2b66bca260603d25db68bccc08e11b69d76d012
#   Address (SS58): 5Hmg8FcLs8BntiybzUqhggd2B6JLF7BbXQsHMvxv8RroRXS4


test_base58()
print(public_to_address('0xfc6c6696498ebf3df05cce70f2b66bca260603d25db68bccc08e11b69d76d012'))

key = PublicKey(b'\0' * 32)
print(key.to_hex())


key = PrivateKey(b'\0' * 32)
print(key.to_hex())


