import asyncio
from websocket import create_connection
import json
import time


class WSClient:
    subscriptions = dict()
    connection = None
    started = False

    def __init__(self, uri):
        self.id = 0
        self.connection = create_connection(uri)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.handle())
        self.loop.run_until_forever()

    async def handle(self):
        while True:
            result = self.connection.recv()
            print(result)

    def subscribe(self, method):
        message = dict()
        self.id += 1
        message["jsonrpc"] = "2.0"
        message["id"] = self.id
        message["params"] = []
        message["method"] = "chain_subscribeNewHead"
        self.connection.send(json.dumps(message))


client = WSClient("ws://192.168.2.158:9944")
client.subscribe('a')

time.sleep(10000)


