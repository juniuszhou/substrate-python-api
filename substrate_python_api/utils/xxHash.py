import xxhash


# data like b'Sudo Key'
def get_xxhash_128(data):
    x = xxhash.xxh64(seed=0)
    x.update(data)
    high = x.digest()
    x = xxhash.xxh64(seed=1)
    x.update(data)
    low = x.digest()
    a = bytearray(low + high)
    a.reverse()
    return '0x' + a.hex()


def test():
    # xxhashAsHex('abc'); // => 0x44bc2cf5ad770999

    x = xxhash.xxh64(seed=0)
    x.update(b"Sudo Key")
    print(x.digest())  # 64 bits 8 bytes
    x = xxhash.xxh64(seed=1)
    x.update(b"Sudo Key")
    print(x.hexdigest())  # 64 bits 8 bytes

    x = xxhash.xxh64(seed=0)
    x.update(b'abc')
    print(x.hexdigest())  # 64 bits 8 bytes



