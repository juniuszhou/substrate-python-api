import asyncio
import websockets
import json
import time
from threading import Thread

class WSClient:
    subscriptions = set()
    connection = None
    loop = None
    started = False
    uri = None

    def __init__(self, uri):
        self.uri = uri

    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()


    async def get_connection(self):
        self.connection = await websockets.connect(uri=self.uri)

    def start(self):
        self.started = True
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.get_connection())
        new_loop = asyncio.new_event_loop()
        t = Thread(target=WSClient.start_loop, args=(new_loop,))
        t.start()
        new_loop.run_until_complete(self.handle())

    async def handle(self):
        print('into handle')
        while True:
            print('in while true')
            data = self.connection.recv()
            print(data)
            time.sleep(1)

    def subscribe(self, subscription):
        print('send to.')
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

