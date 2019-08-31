from substrate_python_api.client.client import WSClient

client = WSClient(uri='ws://192.168.2.158:9944')


def test_system():
    print(client.system_name())
    print(client.system_version())
    print(client.system_chain())
    print(client.system_properties())
    print(client.system_health())
    print(client.system_peers())
    print(client.system_network_state())


test_system()

