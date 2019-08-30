from substrate_python_api.utils.codec import decode_compact_integer, next_byte, hex_to_string
from substrate_python_api.metadata.V7_types import StorageV7, ConstV7, EventArgV7, CallV7, FunctionCallArgV7


def get_storage_v7(data):
    storage = StorageV7()
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


def get_call_v7(data):
    call = CallV7()
    call_name_len, data = decode_compact_integer(data)
    call.name, data = hex_to_string(data[:call_name_len * 2]), data[call_name_len * 2:]

    arg_number, data = decode_compact_integer(data)
    for _ in range(0, arg_number):
        arg = FunctionCallArgV7()
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


def get_event_v7(data):
    event = EventArgV7()
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


def get_const_v7(data):
    event = EventArgV7()
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

def get_const_v7(data):
    const = ConstV7()
    const_name_len, data = decode_compact_integer(data)
    const.name, data = hex_to_string(data[:const_name_len * 2]), data[const_name_len * 2:]

    const_type_len, data = decode_compact_integer(data)
    const.type, data = hex_to_string(data[:const_type_len * 2]), data[const_type_len * 2:]

    const_value_len, data = decode_compact_integer(data)
    const.value, data = data[:const_value_len * 2], data[const_value_len * 2:]

    doc_number, data = decode_compact_integer(data)
    for _ in range(0, doc_number):
        doc_name_len, data = decode_compact_integer(data)
        doc, data = hex_to_string(data[:doc_name_len * 2]), data[doc_name_len * 2:]
        const.doc.append(doc)

    return const, data

