import asyncio
import websocket
import json
import multiprocessing
import time

ws_uri = 'ws://192.168.2.158:9944'

def get_data():
    # ws_uri = 'ws://47.254.169.60:9944'
    conn = websocket.create_connection(ws_uri)

    message = dict()
    message["jsonrpc"] = "2.0"
    message["id"] = 1
    message["params"] = []
    message["method"] = 'chain_subscribeNewHead'
    conn.send(json.dumps(message))
    while True:
        print(conn.recv())
        time.sleep(2)


def dead_loop():
    print('dead loop')
    while True:
        print('I am main')
        time.sleep(1)


t1 = multiprocessing.Process(target=get_data())
t2 = multiprocessing.Process(target=dead_loop())

t1.run()
t2.run()


print('ok')




