from utils.codec import decode_compact_integer, next_byte, hex_to_string
from metadata.metadata_types import StorageV5, EventArgV5, FuncTypeV5, CallV5, FunctionCallArgV5


def get_storage_v5(data):
    storage = StorageV5()
    storage_name_len, data = decode_compact_integer(data)
    storage.name, data = hex_to_string(data[:storage_name_len*2]), data[storage_name_len*2:]

    storage.modifier, data = next_byte(data)
    is_complex_type, data = next_byte(data)

    if is_complex_type == 0:
        storage.type.type = 0
    else:
        storage.type.type, data = next_byte(data)

    type1_len, data = decode_compact_integer(data)
    storage.type.key1, data = hex_to_string(data[:type1_len*2]), data[type1_len*2:]

    # map
    if is_complex_type == 1:
        length, data = decode_compact_integer(data)
        storage.type.value, data = hex_to_string(data[:length*2]), data[length*2:]
    # double map
    elif is_complex_type == 2:
        type2_len, data = decode_compact_integer(data)
        storage.type.value, data = hex_to_string(data[:type2_len*2]), data[type2_len*2:]

        value_length, data = decode_compact_integer(data)
        storage.type.value, data = hex_to_string(data[:value_length*2]), data[value_length*2:]

    if is_complex_type != 0:
        storage.type.isLinked, data = next_byte(data)

    # extract fallback as raw hex
    fallback_len, data = decode_compact_integer(data)
    storage.fallback, data = data[:fallback_len * 2], data[fallback_len * 2:]

    # documents count
    doc_count, data = decode_compact_integer(data)
    for di in range(0, doc_count):
        doc_length, data = decode_compact_integer(data)
        doc, data = hex_to_string(data[:doc_length * 2]), data[doc_length * 2:]
        storage.doc.append(doc)

    return storage, data


def get_call_v5(data):
    call = CallV5()
    call_name_len, data = decode_compact_integer(data)
    call.name, data = hex_to_string(data[:call_name_len * 2]), data[call_name_len * 2:]

    arg_number, data = decode_compact_integer(data)
    for _ in range(0, arg_number):
        arg = FunctionCallArgV5()
        arg_name_len, data = decode_compact_integer(data)
        arg.name, data = hex_to_string(data[:arg_name_len * 2]), data[arg_name_len * 2:]
        arg_type_len, data = decode_compact_integer(data)
        arg.type, data = hex_to_string(data[:arg_type_len * 2]), data[arg_type_len * 2:]

    doc_number, data = decode_compact_integer(data)
    for _ in range(0, doc_number):

        doc_name_len, data = decode_compact_integer(data)
        doc, data = hex_to_string(data[:doc_name_len * 2]), data[doc_name_len * 2:]
        call.doc.append(doc)

    return call, data


def get_event_v5(data):
    event = EventArgV5()
    event_name_len, data = decode_compact_integer(data)
    event.name, data = hex_to_string(data[:event_name_len * 2]), data[event_name_len * 2:]

    arg_number, data = decode_compact_integer(data)
    for _ in range(0, arg_number):

        arg_name_len, data = decode_compact_integer(data)
        arg, data = hex_to_string(data[:arg_name_len * 2]), data[arg_name_len * 2:]
        event.args.append(arg)

    doc_number, data = decode_compact_integer(data)
    for _ in range(0, doc_number):
        doc_name_len, data = decode_compact_integer(data)
        doc, data = hex_to_string(data[:doc_name_len * 2]), data[doc_name_len * 2:]
        event.doc.append(doc)

    return event, data


def get_const_v5(data):
    event = EventArgV5()
    event_name_len, data = decode_compact_integer(data)
    event.name, data = hex_to_string(data[:event_name_len * 2]), data[event_name_len * 2:]

    arg_number, data = decode_compact_integer(data)
    for _ in range(0, arg_number):

        arg_name_len, data = decode_compact_integer(data)
        arg, data = hex_to_string(data[:arg_name_len * 2]), data[arg_name_len * 2:]
        event.args.append(arg)

    doc_number, data = decode_compact_integer(data)
    for _ in range(0, doc_number):
        doc_name_len, data = decode_compact_integer(data)
        doc, data = hex_to_string(data[:doc_name_len * 2]), data[doc_name_len * 2:]
        event.doc.append(doc)

    return event, data


def decode_v5(data):
    for index in range(0, 5):
        _, data = next_byte(data)

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


