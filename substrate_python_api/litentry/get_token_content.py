import asyncio
import websockets
import json
import binascii

from substrate_python_api.utils.blake2 import get_blake2_256


def send_hash():
    identity = '0x3341eab002e77fef32a64004f32a110e680dd06b027cffdce19a8bbc5d078061'
    identity_hash = bytearray.fromhex(identity[2:])
    data = b'LitentryStorage AuthorizedTokens' + identity_hash
    print(get_blake2_256(data))


    message = {"jsonrpc": "2.0",
               "method": "state_getStorage",
               "params": [get_blake2_256(data)],
               "id": 1}

    def deal_with_message(data):
        result = json.loads(data)['result']
        result_bytes = bytearray.fromhex(result[2:])
        print('length of result is {}'.format(len(result_bytes)))
        print(result_bytes[48:51])

        token_hash = result_bytes[:32]
        cost_128 = int.from_bytes(result_bytes[32:48], 'little')
        data_length = int.from_bytes(result_bytes[48:49], 'little')
        data = str(result_bytes[49:95])
        datatype = int.from_bytes(result_bytes[95:103], 'little')
        expired = int.from_bytes(result_bytes[103:], 'little')

        print('hash is ', token_hash)
        print(cost_128, data_length, data, datatype, expired)

    def async_call(message):
        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps(message))
                data = await websocket.recv()
                deal_with_message(data)

        asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.157:9944/'))

    async_call(message)


send_hash()
