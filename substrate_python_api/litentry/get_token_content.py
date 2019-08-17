import asyncio
import websockets
import json

from substrate_python_api.utils.blake2 import get_blake2_256


def send_hash():
    identity = '0x6cc0b3a302de9d84c17a3be3a96ac40efc2ee7834feb770a65fba09e256d768e'
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

        token_hash = result_bytes[:32]
        cost_128 = int.from_bytes(result_bytes[32:48], 'little')
        data = int.from_bytes(result_bytes[48:56], 'little')
        datatype = int.from_bytes(result_bytes[56:64], 'little')
        expired = int.from_bytes(result_bytes[64:], 'little')

        print(token_hash)
        print(cost_128, data, datatype, expired)

    def async_call(message):
        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                await websocket.send(json.dumps(message))
                data = await websocket.recv()
                deal_with_message(data)

        asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.158:9944/'))

    async_call(message)


send_hash()
