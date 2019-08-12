import asyncio
import websockets
import json

ws_uri = 'ws://192.168.1.224:9944'


async def get_connection():
    websockets.connect(ws_uri)


def async_call(command, params=[]):
    async def hello(uri):
        async with websockets.connect(ws_uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = 'chain_subscribeNewHead'
            await websocket.send(json.dumps(message))
            while True:
                data = await websocket.recv()
                print(data)

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


async_call('a')

