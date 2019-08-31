
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

    def __init__(self, uri, debug=False):
        self.uri = uri
        self.rpc_id = 0
        self.sub_id = {}
        self.exit = False
        self.task = None
        self.debug = debug

    def start_bak(self):
        self.connection = create_connection(self.uri)
        self.task = threading.Thread(target=self.handle)
        self.task.start()

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

    def system_name(self):
        return self.simple_call('system_name')

    def system_version(self):
        return self.simple_call('system_version')

    def system_chain(self):
        return self.simple_call('system_chain')

    def system_properties(self):
        return self.simple_call('system_properties')

    def system_health(self):
        return self.simple_call('system_health')

    def system_peers(self):
        return self.simple_call('system_peers')

    def system_network_state(self):
        return self.simple_call('system_networkState')

    def state_get_runtime_version(self, hash=None):
        return self.simple_call('state_getRuntimeVersion')

    def simple_call(self, method_name):
        temp_conn = create_connection(self.uri)
        message = dict()
        message["jsonrpc"] = "2.0"
        message["id"] = self.rpc_id
        self.rpc_id += 1
        message["params"] = []
        message["method"] = method_name
        if self.debug:
            print('send message {}'.format(json.dumps(message)))
        temp_conn.send(json.dumps(message))
        result = temp_conn.recv()
        if self.debug:
            print('receive message {}'.format(result))
        data = json.loads(result)
        return data['result']


# client = WSClient("ws://192.168.2.158:9944")
# print('start client')
# client.subscribe('chain_subscribeNewHead')
# time.sleep(1)
# client.subscribe('chain_subscribeFinalizedHeads')
# time.sleep(1)
# client.subscribe('chain_subscribeNewHead')
# time.sleep(10)
# print('stop client')
# client.stop()


