import time
import asyncio
import functools
from threading import Thread, current_thread, Event
from concurrent.futures import Future
import websockets
import json


class B(Thread):
    def __init__(self, start_event):
        Thread.__init__(self)
        self.loop = None
        self.tid = None
        self.event = start_event
        self.uri = 'ws://192.168.2.158:9944/'
        self.connection = None

    async def get_connection(self):
        self.connection = await websockets.connect(uri=self.uri)

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.get_connection())
        self.loop.run_until_complete(self._subscribe())
        self.tid = current_thread()
        self.loop.call_soon(self.event.set)
        self.loop.run_forever()

    def pprint(self):
        self.add_task(self.test())

    async def get_value(self, callback):
        pass

    def println(self):
        print('into println')

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)

    @asyncio.coroutine
    async def test(self):
        while True:
            print("running")
            data = await self.connection.recv()
            print(data)
            await asyncio.sleep(1)

    async def _subscribe(self):
        message = dict()
        message["jsonrpc"] = "2.0"
        message["id"] = 1
        message["params"] = []
        message["method"] = 'chain_subscribeNewHead'
        print('send sub message')
        await self.connection.send(json.dumps(message))

    def add_task(self, coro):
        """this method should return a task object, that I
          can cancel, not a handle"""

        def _async_add(func, fut):
            try:
                ret = func()
                fut.set_result(ret)
            except Exception as e:
                fut.set_exception(e)

        f = functools.partial(asyncio.ensure_future, coro, loop=self.loop)
        if current_thread() == self.tid:
            return f()  # We can call directly if we're not going between threads.
        else:
            # We're in a non-event loop thread so we use a Future
            # to get the task from the event loop thread once
            # it's ready.
            fut = Future()
            self.loop.call_soon_threadsafe(_async_add, f, fut)
            return fut.result()

    def cancel_task(self, task):
        self.loop.call_soon_threadsafe(task.cancel)


event = Event()
b = B(event)
b.start()
event.wait()  # Let the loop's thread signal us, rather than sleeping
b.pprint()

b.println()
time.sleep(10)

b.stop()
