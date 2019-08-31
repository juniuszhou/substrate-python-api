import asyncio
import websockets
import json
import threading

ws_uri = 'ws://192.168.2.158:9944/'


# ws_uri = 'ws://127.0.0.1:9944/'


def async_call(command, params=[], callback=None, debug=False):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = command
            if debug:
                print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
            await websocket.send(json.dumps(message))
            data = await websocket.recv()
            if debug:
                print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
            if callback is not None:
                callback(data)

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


def async_subscribe(method, params=[], callback=None, debug=False):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = method
            if debug:
                print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
            await websocket.send(json.dumps(message))
            while True:
                data = await websocket.recv()
                if debug:
                    print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
                callback(data)

    asyncio.get_event_loop().run_until_complete(hello(ws_uri))


def async_backend_subscribe(method, params=[], callback=None, debug=False):
    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            message = dict()
            message["jsonrpc"] = "2.0"
            message["id"] = 1
            message["params"] = params
            message["method"] = method
            if debug:
                print('Send: >>>> {}'.format(json.dumps(message, indent=4)))
            await websocket.send(json.dumps(message))
            while True:
                data = await websocket.recv()
                if debug:
                    print('Receive: <<<< {}'.format(json.dumps(json.loads(data), indent=4)))
                callback(data)

    asyncio.new_event_loop().run_until_complete(hello(ws_uri))


def backend_sub(method, params=[], callback=None, debug=False):
    t = threading.Thread(target=async_backend_subscribe, args=(method, params, callback, debug))
    t.start()
    return t

