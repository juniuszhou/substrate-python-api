import asyncio
import websockets
import json

# ws_uri = "wss://poc3-rpc.polkadot.io/"
# ws_uri = "wss://substrate-rpc.parity.io/"
# ws_uri = "ws://45.76.157.229:9944/"

ws_uri = 'ws://192.168.1.224:9944/'


def async_call(command, params=[]):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = command
            print(json.dumps(message))
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            print(data)

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))

