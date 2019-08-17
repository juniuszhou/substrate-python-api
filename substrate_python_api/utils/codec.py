# get the first byte as int from hex string.
def next_byte(data):
    a = int(data[0], 16) * 16 + int(data[1], 16)
    return a, data[2:]


def int_to_byte(number):
    return number // 8 * 10 + number % 8


def hex_to_string(hex_data):
    return bytearray.fromhex(hex_data).decode()


def decode_compact_integer(data):
    first_byte, data = next_byte(data)

    flag = first_byte & 0b00000011
    number = 0
    multiplier = 256

    if flag == 0:
        number = first_byte / 4
    elif flag == 1:
        second_byte, data = next_byte(data)
        number = ((first_byte & 0b11111100) + second_byte * 256) // 4
    elif flag == 2:
        number = first_byte
        for i in range(0, 4):
            newBytes, data = next_byte(data)
            number += newBytes * multiplier
            multiplier *= 256
        number = number / 4
    elif flag == 3:
        bytes_count = first_byte // 4 + 4
        for i in range(0, bytes_count):
            newBytes, data = next_byte(data)
            number += newBytes * multiplier
            multiplier *= 256
    else:
        raise Exception('wrong flag.')

    return int(number), data


def encode_compact_integer(number):
    if number <= 63:
        return bytes([number << 2])
    elif number < 64 * 256:
        result = list()
        result.append(((number & 0x3F) << 2) | 0x01)
        result.append(number // 64)
        return bytes(result)
    elif number < 64 * 256 * 256:
        result = list()
        result.append(((number & 0x3F) << 2) | 0x10)
        result.append((number // 64) & 0xFF)
        result.append(number // (64 * 256))
        return bytes(result)
    else:
        result = list()
        result.append(((number & 0x3F) << 2) | 0x11)
        number = number // 64
        while number > 0:
            result.append(number & 0xFF)
            number = number // 256
        return bytes(result)


def encode_test():
    print(encode_compact_integer(60))
    print(encode_compact_integer(1024))
    print(encode_compact_integer(1024*256))
    print(encode_compact_integer(1024 * 256 * 256 * 256))


def decode_test():
    print(decode_compact_integer('3635c9adc5dea00000'))


def encode_example():
    hex_string = '123456'
    bytes_array = bytearray.fromhex(hex_string)
    u8_list = [x for x in bytes_array]

    print(bytes_array)
    print(u8_list)

    print(bytearray.hex(bytes_array))
    print(bytes(u8_list))


def encode_u64_bytes(data):
    return data.to_bytes(8, 'little')


def decode_transfer_extrinsic(bytes_array):
    print('transfer extrinsic length is {}'.format(len(bytes_array)))
    print('version is {}'.format([x for x in bytes_array[:1]]))
    print('separate is {}'.format(bytes_array[1]))
    print('sender is {}'.format([x for x in bytes_array[2:34]]))
    print('signature is {}'.format([x for x in bytes_array[34:98]]))
    print('extra is {}'.format([x for x in bytes_array[98:103]]))
    print('separate is {}'.format(bytes_array[103]))
    print('to is {}'.format([x for x in bytes_array[104:136]]))
    print('amount is {}'.format([x for x in bytes_array[136:]]))
    pass


def decode_logs(data):
    pass

