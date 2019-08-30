from substrate_python_api.utils.codec import next_byte, decode_compact_integer
from substrate_python_api.metadata.V5 import get_storage_v5, get_call_v5, get_event_v5
from substrate_python_api.metadata.V5_types import ModuleV5


def decode_v5(data):

    module_len, data = decode_compact_integer(data)
    print('mLen is {}'.format(module_len))

    for moduleIndex in range(0, module_len):
        mv = ModuleV5()

        name_len, data = decode_compact_integer(data)
        name, data = data[:name_len*2], data[name_len*2:]
        print('module name is {}, len is {}'.format(bytearray.fromhex(name).decode(), name_len))

        prefix_len, data = decode_compact_integer(data)
        prefix, data = data[:prefix_len*2], data[prefix_len*2:]
        print('prefix name is {}, len is {}'.format(bytearray.fromhex(prefix).decode(), prefix_len))

        storage_is_set, data = next_byte(data)
        if storage_is_set != 0:
            storage_len, data = decode_compact_integer(data)
            for i in range(0, storage_len):
                storage, data = get_storage_v5(data)
                print('>>>> storage {}'.format(storage.name))
                mv.storage.append(storage)

        call_is_set, data = next_byte(data)
        if call_is_set != 0:
            call_len, data = decode_compact_integer(data)
            for i in range(0, call_len):
                call, data = get_call_v5(data)
                print('>>>> call {}'.format(call.name))
                mv.call.append(call)

        event_is_set, data = next_byte(data)
        if event_is_set != 0:
            event_len, data = decode_compact_integer(data)
            for i in range(0, event_len):
                event, data = get_event_v5(data)
                print('>>>> event {}'.format(event.name))
                mv.event.append(event)



