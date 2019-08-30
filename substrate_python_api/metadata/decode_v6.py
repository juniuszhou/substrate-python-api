from substrate_python_api.utils.codec import next_byte, decode_compact_integer, hex_to_string
from substrate_python_api.metadata.V5 import get_storage_v5, get_call_v5, get_event_v5
from substrate_python_api.metadata.V6 import get_const_v6
from substrate_python_api.metadata.V6_types import ModuleV6


def decode_v6(data):
    module_len, data = decode_compact_integer(data)
    print('module length is {}'.format(module_len))

    for moduleIndex in range(0, module_len):
        mv = ModuleV6()
        mv.index = moduleIndex

        name_len, data = decode_compact_integer(data)
        name, data = data[:name_len*2], data[name_len*2:]
        print('module name is {}, index is {}'.format(bytearray.fromhex(name).decode(), moduleIndex))

        # if 0x01 means following is prefix. 0x00 not prefix.
        if_prefix, data = next_byte(data)
        if if_prefix != 0:
            prefix_len, data = decode_compact_integer(data)
            prefix, data = data[:prefix_len*2], data[prefix_len*2:]
            print('prefix name is {}, len is {}'.format(bytearray.fromhex(prefix).decode(), prefix_len))

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
                call.index = i
                print('>>>> call {} index is {}'.format(call.name, i))
                mv.call.append(call)

        event_is_set, data = next_byte(data)
        if event_is_set != 0:
            event_len, data = decode_compact_integer(data)
            for i in range(0, event_len):
                event, data = get_event_v5(data)
                print('>>>> event {}'.format(event.name))
                mv.event.append(event)

        const_len, data = decode_compact_integer(data)
        for i in range(0, const_len):
            const, data = get_const_v6(data)
            print('>>>> event {}'.format(const.name))
            mv.event.append(const)




