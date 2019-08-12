import asyncio
import websockets
import json


messages = [{"jsonrpc": "2.0", "method": "state_getStorageHash", "params": ["0x00"], "id": 1},
    {"jsonrpc": "2.0", "method": "state_getStorageSize", "params": ["0x00"], "id": 1},
]

def deal_with_message(data):
    print(data)


def async_call(message):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            deal_with_message(data)

    asyncio.get_event_loop().run_until_complete(hello('ws://localhost:9944/'))

for message in messages:
   async_call(message)

