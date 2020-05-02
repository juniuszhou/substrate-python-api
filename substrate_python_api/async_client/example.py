import time
import asyncio
import functools
from threading import Thread, current_thread, Event

from concurrent.futures import Future
import websockets
import json
import sys

class C():
    def __init__(self):
        self.loop = None
        self.uri = 'ws://192.168.2.158:9944/'
        self.connection = None
        self.task = None
        self.pill2kill = None

    async def get_connection(self):
        self.connection = await websockets.connect(uri=self.uri)

    async def close_connection(self):
        await self.connection.close()

    def start_back(self):
        print('start_back')
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        self.loop.run_until_complete(self.test())

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.get_connection())
        self.pill2kill = Event()
        self.loop.call_soon_threadsafe(self.start_back())
        # self.loop.run_until_complete(self._subscribe())
        # self.loop.run_forever()

    def println(self):
        print('into println')

    def sub(self):
        self.loop.run_until_complete(self._subscribe())

    def stop(self):
        print('into stop')
        self.close_connection()
        self.pill2kill.set()
        self.task.join()

        # self.loop.run_until_complete(self.loop.stop)
        # current_thread().
        # sys.exit()
        time.sleep(1)
        print('wait for task end.')

        self.loop.close()

    async def test(self):
        while not self.pill2kill.is_set():
            print("running")
            data = await self.connection.recv()
            print(data)
        print('out of test')

    async def _subscribe(self):
        message = dict()
        message["jsonrpc"] = "2.0"
        message["id"] = 1
        message["params"] = []
        message["method"] = 'chain_subscribeNewHead'
        print('send sub message')
        await self.connection.send(json.dumps(message))


client = C()
client.run()
client.sub()

time.sleep(5)
print('try to stop')
client.stop()
