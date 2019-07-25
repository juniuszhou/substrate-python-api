import xxhash
x = xxhash.xxh64(seed=0)
x.update(b'Nobody inspects')
print(x.digest())  # 64 bits 8 bytes


x = xxhash.xxh64(seed=1)
x.update(b'Nobody inspects')
print(x.digest())  # 64 bits 8 bytes







