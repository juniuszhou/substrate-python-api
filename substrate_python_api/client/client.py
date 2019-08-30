import asyncio
from websocket import create_connection
import websockets
import json
import time


class WSClient:
    subscriptions = dict()
    connection = None
    started = False

    def __init__(self, uri):
        self.uri = uri
        self.id = 0
        self.connection = create_connection(uri)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.handle())
        self.loop.run_until_forever()

    async def handle(self):
        while True:
            result = self.connection.recv()
            print(result)

    def async_call(self, command, params=[], callback=None, debug=False):
        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                message = dict()
                message["jsonrpc"] = "2.0"
                message["id"] = 1
                message["params"] = params
                message["method"] = command
                if debug:
                    print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
                await websocket.send(json.dumps(message))
                data = await websocket.recv()
                if debug:
                    print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
                if callback is not None:
                    callback(data)

        asyncio.get_event_loop().run_until_complete(hello(self.uri))

    def async_subscribe(self, method, params=[], callback=None, debug=False):
        async def hello(uri):
            async with websockets.connect(uri) as websocket:
                message = dict()
                message["jsonrpc"] = "2.0"
                message["id"] = 1
                message["params"] = params
                message["method"] = method
                if debug:
                    print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
                await websocket.send(json.dumps(message))
                while True:
                    data = await websocket.recv()
                    if debug:
                        print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
                    callback(data)

        asyncio.get_event_loop().run_until_complete(hello(self.uri))


client = WSClient("ws://192.168.2.158:9944")
client.subscribe('a')

time.sleep(10000)


