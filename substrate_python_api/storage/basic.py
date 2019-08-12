import asyncio
import websockets
import json

# for some well known storage. seems just code can be got easily.

# key = "0x" + b":code".hex()
key = "0x" + b"templateModule something".hex()
print(key)

message = {"jsonrpc": "2.0", "method": "state_getStorage", "params": [key], "id": 1}


def deal_with_message(data):
    print(data)


def async_call(message):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            deal_with_message(data)

    asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.158:9944/'))


async_call(message)


