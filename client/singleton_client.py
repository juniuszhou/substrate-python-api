import asyncio
import websockets
import json
import time


class WSClient():
    subscriptions = set()
    connection = None
    started = False
    uri = None

    def __init__(self, uri):
        self.uri = uri
        self.loop = asyncio.get_event_loop()
        # self.get_connection()

    def start(self):
        self.started = True
        self.loop.run_until_complete(self.handle())
        # self.loop.run_forever()  # problematic, because it does not allow new subscribe() events

    async def handle(self):
        if self.connection is not None:
            # listen to every websocket
            futures = self.listen(self.connection)
            done, pending = await asyncio.wait(futures)

            # the following is apparently necessary to avoid warnings
            # about non-retrieved exceptions etc
            try:
                data, ws = done.pop().result()
            except Exception as e:
                print("OTHER EXCEPTION", e)

            for task in pending:
                task.cancel()

    async def get_connection(self):
        print('get connection')
        self.connection = await websockets.connect(self.uri)
        print('get connection done')

    async def listen(self, ws):
        try:
            async for data in ws:
                data = json.loads(data)
                print('got data is {}'.format(data))
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

    def restart_socket(self, ws):
        pass
    #     for s in self.subscriptions:
    #         if s.ws == ws and not s.ws.connected:
    #             print(s)
    #             del self.connections[s.url]
    #             self.subscribe(s)


ws_uri = 'ws://192.168.2.158:9944/'
client = WSClient(ws_uri)
client.subscribe(None)


time.sleep(1000)