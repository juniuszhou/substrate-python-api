from metadata.common_algo import next_byte, decode_compact_integer, hex_to_string
from metadata.V5 import get_storage_v5, get_call_v5, get_event_v5
from metadata.metadata_types import ModuleV5
from metadata.decode_v5 import decode_v5
from metadata.decode_v6 import decode_v6


def decode_metadata(data):
    print('decode_metadata start .......................')
    version = data[:10]
    print(version)
    print('version is {}'.format(bytearray.fromhex(version).decode()))
    print(data[10:])
    decode_v6(data[10:])





