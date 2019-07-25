import asyncio
import websockets
from websockets import WebSocketClientProtocol

class SWebsocket(object):

    def __init__(self, websocket: WebSocketClientProtocol):
        self.ws = websocket
        self.queues = {}
        self.subscribe()

    def subscribe(self):
        # fire and forget function
        asyncio.ensure_future(self.recv_mess())

    async def recv_mess(self):
        while True:
            try:
                data = await self.ws.recv()
            except websockets.ConnectionClosed as e:
                for _, q in self.queues.items():
                    await q.put(e)
                return
            for _, q in self.queues.items():
                await q.put(data)

    async def recv(self, id):
        # read value from queue
        if id not in self.queues:
            self.queues[id] = asyncio.Queue()
        data = await self.queues[id].get()
        if isinstance(data, websockets.ConnectionClosed):
            raise data
        return data



