import asyncio
import websockets
import json
import time


class WSClient:
    subscriptions = set()
    connection = None
    loop = None
    started = False
    uri = None

    def __init__(self, uri):
        self.uri = uri

    def start(self):
        self.started = True
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.handle())

    async def handle(self):
        time.sleep(1)
        if self.connection is None:
            self.connection = await websockets.connect(self.uri)
        while True:
            data = self.connection.recv()
            print(data)
            time.sleep(1)

    def subscribe(self, subscription):
        self.connection.send(subscription)

    async def _subscribe(self, subscription):
        try:
            if self.connection is None:
                await self.get_connection()
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = []
            message["method"] = 'chain_subscribeNewHead'
            print('send sub message')
            await self.connection.send(json.dumps(message))
            self.subscriptions.add(subscription)
        except Exception as e:
            print("ERROR SUBSCRIBING; RETRYING", e)
            await asyncio.sleep(2)
            self.subscribe(subscription)


ws_uri = 'ws://192.168.2.158:9944/'
client = WSClient(ws_uri)
client.start()
print('client started.')
client.subscribe(None)


time.sleep(1000)

