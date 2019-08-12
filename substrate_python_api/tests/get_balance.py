import asyncio
import websockets
import json
from substrate_python_api.utils.blake2 import get_blake2_256
import base58

address = b"5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
result = base58.b58decode(b'5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY')

balance = b'Balances FreeBalance' + result[1:33]
print([x for x in b'Balances FreeBalance'])
array = bytearray(result[1:33])
print([x for x in array])
print(get_blake2_256(balance))

message = {"jsonrpc": "2.0",
           "method": "state_getStorage",
           "params": [get_blake2_256(balance)],
           "id": 1}


def deal_with_message(data):
    a = json.loads(data)['result']
    print(a[2:])
    print(int.from_bytes(bytearray.fromhex(a[2:]), byteorder='little'))


def async_call(message):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            deal_with_message(data)

    asyncio.get_event_loop().run_until_complete(hello('ws://192.168.2.158:9944/'))


async_call(message)
