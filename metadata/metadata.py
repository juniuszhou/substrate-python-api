import asyncio
import websockets
import json
from ethereum.utils import decode_hex
from polkadot.metadata.lib import decode_v5

# ws_uri = "wss://poc3-rpc.polkadot.io/"
# ws_uri = "wss://substrate-rpc.parity.io/"
# ws_uri = "ws://45.76.157.229:9944/"

ws_uri = 'ws://192.168.2.158:9944/'


def async_call(command, params=[]):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = command
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            result = json.loads(data)['result']
            print(result)
            print(result[0], result[1], result[2])
            print(decode_hex(result))
            decode_v5(result[2:])
            # print(bytearray.fromhex(result).decode())

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


async_call('state_getMetadata')
