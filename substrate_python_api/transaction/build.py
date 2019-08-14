from substrate_python_api.utils.codec import decode_compact_integer

# hex from integer to hex string.
SEPARATE = bytes([255])
print(SEPARATE)


def extrinsic_to_bytes():  # fix length 134 + flexible.
    # length of whole extrinsic        n bytes
    # version of signature 0x81 0x82   1 byte
    # separate 0xFF                    1 byte
    # sender public key                32 bytes
    # singature                        64 byte
    # extra era                        1 byte
    # extra nonce                      1 byte
    # extra weight                     1 byte
    # extra take fee                   1 byte
    # module id and method id          1+1 byte
    # separate 0xFF                    1 byte
    # function and its parameters      n byte (address 24 bytes)
    pass




