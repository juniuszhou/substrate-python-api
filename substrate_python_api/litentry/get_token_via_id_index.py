import asyncio
import websockets
import json

from substrate_python_api.utils.blake2 import get_blake2_256
from substrate_python_api.utils.codec import encode_compact_integer


def send_hash():
    identity = '0x672576b52b8b52d2d8a9e6aafa06654d269b1f98b2598d7f3e6bc98fdd3790c7'
    identity_hash = bytearray.fromhex(identity[2:])
    index = encode_compact_integer(0)
    index = index * 8
    data = b'LitentryStorage IdentityAuthorizedTokensArray' + identity_hash + index
    print(get_blake2_256(data))

    message = {"jsonrpc": "2.0",
               "method": "state_getStorage",
               "params": [get_blake2_256(data)],
               "id": 1}

    def deal_with_message(data):
        print(data)

    def async_call(message):
        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps(message))
                data = await websocket.recv()
                deal_with_message(data)

        asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.158:9944/'))

    async_call(message)


send_hash()
