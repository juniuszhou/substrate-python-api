
from websocket import create_connection
import json
import time
import threading

subscribe_methods = [
    '',
]

rpc_methods = [
    '',
]


class WSClient:
    subscriptions = dict()
    connection = None
    started = False

    def __init__(self, uri):
        self.uri = uri
        self.id = 0
        self.connection = create_connection(uri)
        self.task = threading.Thread(target=self.handle)
        self.task.start()
        self.sub_id = None
        self.exit = False

    def handle(self):
        print('handle')
        while not self.exit:
            print('into while true')
            result = self.connection.recv()
            data = json.loads(result)
            if data.get('result'):
                self.sub_id = data['result']
                print('sub id is {}'.format(self.sub_id))
            print(result)

    def subscribe(self, sub):
        message = dict()
        message["jsonrpc"] = "2.0"
        message["id"] = 1
        message["params"] = []
        message["method"] = sub
        print('send sub message')
        self.connection.send(json.dumps(message))

    def stop(self):
        self.exit = True
        message = dict()
        message["jsonrpc"] = "2.0"
        message["id"] = 2
        sub_list = list()
        sub_list.append(self.sub_id)
        message["params"] = sub_list
        message["method"] = 'chain_unsubscribeNewHead'
        print('send sub message {}'.format(json.dumps(message)))
        self.connection.send(json.dumps(message))
        # self.connection.close()
        self.task.join()

    def system_version(self):
        pass


client = WSClient("ws://192.168.2.158:9944")
print('start client')
client.subscribe('chain_subscribeNewHead')
time.sleep(1)
client.subscribe('chain_subscribeFinalizedHeads')
time.sleep(1)
client.subscribe('chain_subscribeNewHead')
time.sleep(10)
print('stop client')
client.stop()


