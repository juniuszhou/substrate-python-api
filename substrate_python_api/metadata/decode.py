from substrate_python_api.metadata.decode_v0 import decode_v0
from substrate_python_api.metadata.decode_v4 import decode_v4
from substrate_python_api.metadata.decode_v5 import decode_v5
from substrate_python_api.metadata.decode_v6 import decode_v6
from substrate_python_api.metadata.decode_v7 import decode_v7
from substrate_python_api.utils.codec import decode_compact_integer


def decode_metadata(data):
    print('decode_metadata start .......................')
    print(data)
    meta_version = data[:10]
    version = int(meta_version[8:])
    print('version is {}'.format(version))

    if version == 0:
        decode_v0(data[10:])
    elif version == 4:
        decode_v4(data[10:])

    elif version == 5:
        decode_v5(data[10:])

    elif version == 6:
        decode_v6(data[10:])
    elif version == 7:
        decode_v7(data[10:])


def test():
    # test data from metadata in file.

    pass



