from substrate_python_api.metadata.decode_v4 import decode_v4
from substrate_python_api.metadata.decode_v5 import decode_v5
from substrate_python_api.metadata.decode_v6 import decode_v6
from substrate_python_api.metadata.decode_v7 import decode_v7
from substrate_python_api.utils.codec import decode_compact_integer
from substrate_python_api.metadata.metadata_types import Metadata


def decode_metadata(data):
    print('decode_metadata start .......................')
    meta_version = data[:10]
    version = int(meta_version[8:])
    print('version is {}'.format(version))

    if version == 0:
        raise Exception('deprecated metadata version {}'.format(version))
    elif version == 4:
        metadata = decode_v4(data[10:])
    elif version == 5:
        metadata = decode_v5(data[10:])
    elif version == 6:
        metadata = decode_v6(data[10:])
    elif version == 7:
        metadata = decode_v7(data[10:])
    else:
        raise Exception('not supported metadata version {}'.format(version))

    return metadata
