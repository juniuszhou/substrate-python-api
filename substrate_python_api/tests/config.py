import asyncio
import websockets
import json

ws_uri = 'ws://192.168.2.158:9944/'
# ws_uri = 'ws://127.0.0.1:9944/'

def async_call(command, params=[], callback=None):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = command
            print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
            if callback is not None:
                callback(data)

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


