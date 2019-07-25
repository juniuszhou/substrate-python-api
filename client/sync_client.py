from websocket import create_connection
import json
import threading
import time


class Client(threading.Thread):
    # uri format ws://192.168.2.158:9944
    def __init__(self, uri):
        self.ws = create_connection("ws://192.168.2.158:9944")
        self.id = 0
        self.subs = dict()
        threading.Thread.__init__(self)
        self.loop()

    def get_message(self, method, params):
        message = dict()
        self.id += 1
        message["jsonrpc"] = "2.0"
        message["id"] = self.id
        message["params"] = []
        message["method"] = "chain_subscribeNewHead"
        return json.dumps(message)

    def send(self, method, params):
        self.ws.send(self.get_message(method, params))

    def sub(self, method, params, callback):
        self.ws.send(self.get_message(method, params))
        self.subs[self.id] = callback

    def loop(self):
        while True:
            response = self.ws.recv()
            print(response)


# ws.connection("ws://192.168.2.158:9944")

client = Client('a')
callback = lambda message: print(message)
client.start()
print('ok')
client.sub('a', [], callback)
time.sleep(10)





