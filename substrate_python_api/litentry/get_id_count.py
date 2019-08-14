import asyncio
import websockets
import json

from substrate_python_api.utils.xxHash import get_xxhash_128
from substrate_python_api.utils.codec import encode_compact_integer


def send_hash():

    message = {"jsonrpc": "2.0",
               "method": "state_getStorage",
               "params": [get_xxhash_128(b'LitentryStorage IdentitiesCount')],
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
