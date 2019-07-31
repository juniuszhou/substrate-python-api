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


key = PublicKey(b'\0' * 32)
print(key.to_hex())


key = PrivateKey(b'\0' * 32)
print(key.to_hex())


