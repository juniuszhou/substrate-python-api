import asyncio
import websockets
import json

from substrate_python_api.utils.blake2 import get_blake2_256
from substrate_python_api.utils.codec import encode_u64_bytes


def send_hash():
    index = encode_u64_bytes(0)
    print(index)
    data = b'LitentryStorage IdentitiesArray' + index
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
