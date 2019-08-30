# util_crypto.xxhashAsHex(util.stringToU8a("Sudo Key"), 128)
# "0x50 a6 3a 87 1a ce d2 2e 88ee6466fe5aa5d9"

# 2ed2ce1a873aa650
# d9a55afe6664ee88

import asyncio
import websockets
import json
from substrate_python_api.utils.xxHash import get_xxhash_128


def send_hash():
    print(get_xxhash_128('LitentryModule IdentitiesCount'))
    message = {"jsonrpc": "2.0",
               "method": "state_getStorage",
               # "params": ["0x7f864e18e3dd8b58386310d2fe0919eef27c6e558564b7f67f22d99d20f587bb"],
               "params": [get_xxhash_128('Sudo Key')],
               # "params": [get_xxhash_128('System Events')],
               # "params": [get_hash_128('LitentryStorage IdentitiesCount')],
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
