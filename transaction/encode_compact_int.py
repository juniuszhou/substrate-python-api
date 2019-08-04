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


def test():
    print(encode_compact_integer(60))
    print(encode_compact_integer(1024))
    print(encode_compact_integer(1024*256))
    print(encode_compact_integer(1024 * 256 * 256 * 256))


test()

