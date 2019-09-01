import binascii


# hexlify is change asc to bytes
def test_hexlify():
    a = b'0123456789abcdef'
    print(binascii.hexlify(a), len(binascii.hexlify(a)))
    print(bytearray.fromhex(a.hex()))


def test_unhexlify():
    a = b'30313233343536373839616263646566'
    print(binascii.unhexlify(a), len(binascii.unhexlify(a)))


def test_hex_bytes():
    result = bytes(bytearray.fromhex('30313233343536373839616263646566'))
    print(result)


test_unhexlify()
# test_hexlify()
#
test_hex_bytes()
