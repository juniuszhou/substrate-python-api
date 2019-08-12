from utils.codec import decode_compact_integer, next_byte, hex_to_string
from metadata.metadata_types import ConstV6


def get_const_v6(data):
    const = ConstV6()
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

