# get the first byte as int from hex string.
def next_byte(data):
    a = int(data[0], 16) * 16 + int(data[1], 16)
    return a, data[2:]


# get the length of next item from hex string.
# four types according to postfix in first byte.
# 0~63 bytes as X * 4
# 64 * X + Y bytes, Y in second byte and X*4+1 in first byte.
# actual length * 4 + 2. with small endian.
#
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


def hex_to_string(hex_data):
    return bytearray.fromhex(hex_data).decode()





