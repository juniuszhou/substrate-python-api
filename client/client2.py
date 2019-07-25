import asyncio
import websockets
import json
import time


class WSClient():
    subscriptions = set()
    connection = None
    started = False
    loop = None

    def __init__(self):
        self.connection = websockets.connect("ws://192.168.2.158:9944")
        print('connection is OK.')

    async def start(self):
        self.loop = asyncio.get_event_loop()
        await self.loop.run_until_complete(self.handle())

    async def handle(self):
        while True:
            await asyncio.sleep(1000)
            # listen to every websocket
            futures = [self.listen(self.connections[url]) for url in self.connections]
            done, pending = await asyncio.wait(futures)

            # the following is apparently necessary to avoid warnings
            # about non-retrieved exceptions etc
            try:
                data, ws = done.pop().result()
            except Exception as e:
                print("OTHER EXCEPTION", e)

            for task in pending:
                task.cancel()

    async def listen(self, ws):
        try:
            async for data in ws:
                data = json.loads(data)
                # call the subscriber (listener) back when there's data
                [s.listener._handle_result(data) for s in self.subscriptions if s.ws == ws]
        except Exception as e:
            print('ERROR LISTENING; RESTARTING SOCKET', e)
            await asyncio.sleep(2)
            self.restart_socket(ws)

    def subscribe(self, subscription):
        task = self.loop.create_task(self._subscribe(subscription))
        asyncio.gather(task)

        if not self.started:
            self.start()

    async def _subscribe(self, subscription):
        try:
            ws = self.connections.get(subscription.url, await websockets.connect(subscription.url))
            await ws.send(json.dumps(subscription.sub_msg))

            subscription.ws = ws
            self.connections[subscription.url] = ws
            self.subscriptions.add(subscription)
        except Exception as e:
            print("ERROR SUBSCRIBING; RETRYING", e)
            await asyncio.sleep(2)
            self.subscribe(subscription)

    def restart_socket(self, ws):
        for s in self.subscriptions:
            if s.ws == ws and not s.ws.connected:
                print(s)
                del self.connections[s.url]
                self.subscribe(s)


client = WSClient()

def my_sleep():
    time.sleep(1000)
asyncio.run(my_sleep)
print('client is build.')


