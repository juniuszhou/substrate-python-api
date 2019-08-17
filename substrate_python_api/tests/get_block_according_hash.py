from substrate_python_api.tests.config import async_call
import json
from substrate_python_api.utils.codec import hex_to_string, decode_transfer_extrinsic
message = {"jsonrpc": "2.0", "method": "chain_getBlock", "params": [], "id": 2}


def get_block(data):
    json_data = json.loads(data)
    header = json_data['result']['block']['header']
    extrinsics = json_data['result']['block']['extrinsics']
    print('header is {}'.format(header))
    # bytes_array = bytearray.fromhex(header['digest']['logs'][0][2:])
    # print(hex_to_string(extrinsics[0][2:]))
    bytes_array = bytearray.fromhex(extrinsics[1][2:])
    decode_transfer_extrinsic(bytes_array)
    print([x for x in bytes_array])


# a block include transfer transaction.
block_hash = '0x028271f752ed8bfa982cf0a12186eeb24214f0018daf5166e00ba9b09c1a565a'
async_call("chain_getBlock", [block_hash], get_block)



