import asyncio
import websockets
import websocket
import json

from substrate_python_api.metadata.decode import decode_metadata

ws_uri = 'ws://192.168.2.158:9944/'


def async_call(uri='ws://127.0.0.1:9944/'):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = []
            message["method"] = 'state_getMetadata'
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            result = json.loads(data)['result']
            decode_metadata(result[2:])
    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


def sync_call(uri='ws://127.0.0.1:9944/'):
    ws = websocket.create_connection(uri)
    message = dict()
    message["jsonrpc"] = "2.0"
    message["id"] = 1
    message["params"] = []
    message["method"] = 'state_getMetadata'
    ws.send(json.dumps(message))
    data = ws.recv()
    result = json.loads(data)['result']
    return decode_metadata(result[2:])


def test():
    result = sync_call('ws://192.168.2.158:9944/')
    print('result is ')
    print(result)

test()