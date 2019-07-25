from websockets import client

class Client:
    pass

import asyncio
import websockets
import json

# ws_uri = "wss://poc3-rpc.polkadot.io/"
# ws_uri = "wss://substrate-rpc.parity.io/"
# ws_uri = "ws://45.76.157.229:9944/"

ws_uri = 'ws://192.168.2.158:9944/'

client = websockets.connect(ws_uri)
client.send('/close')
print(client)



# def async_call():
#     async def hello(uri):
#             async with websockets.connect(uri) as websocket:
#                 return websocket
#
#     asyncio.get_event_loop().run_until_complete(hello(ws_uri))
#     asyncio.get_event_loop().run_forever()
#
#
# ws = async_call()
#
# message = dict()
# message["jsonrpc"] = "2.0"
# message["id"] = 1
# message["params"] = []
# message["method"] = 'system_name'
# ws.send(json.dumps(message))
# data = ws.recv()
# print(data)


