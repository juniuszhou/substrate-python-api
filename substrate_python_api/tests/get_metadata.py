import asyncio
import websockets
import json

from substrate_python_api.metadata.decode import decode_metadata

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
            decode_metadata(result[2:])
            # print(bytearray.fromhex(result).decode())

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


async_call('state_getMetadata')
