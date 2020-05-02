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
        self.t = None

    async def get_connection(self):
        self.connection = await websockets.connect(uri=self.uri)

    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def start(self):
        self.started = True
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.get_connection())
        print('start')
        self.start_handle()
        self.loop.run_forever()

    def start_handle(self):
        print('into start_handle')
        new_loop = asyncio.new_event_loop()
        worker = Thread(target=self.handle_loop, args=(new_loop,))
        worker.start()
        new_loop.run_forever()

    def handle_loop(self, loop):
        print('into handle loop')
        asyncio.set_event_loop(loop)
        self.handle()

    async def handle(self):
        print('into handle')
        while True:
            print('in while true')
            data = await self.connection.recv()
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
time.sleep(2)
client.subscribe(None)

time.sleep(1000)
