from metadata.decode_v6 import decode_v6


def decode_metadata(data):
    print('decode_metadata start .......................')
    version = data[:10]
    print(version)
    print('version is {}'.format(bytearray.fromhex(version).decode()))
    print(data[10:])
    decode_v6(data[10:])





