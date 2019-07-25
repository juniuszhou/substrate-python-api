import asyncio
import websockets
import json

message = {"jsonrpc": "2.0", "method": "state_call", "params": ["0x00", "0x00"], "id": 1}


def deal_with_message(data):
    print(data)


def async_call():
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            deal_with_message(data)

    asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.158:9944/'))


async_call()
