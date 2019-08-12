import base58


def test_base58():
    test_str = b"1234"
    print(base58.b58encode(test_str))

    test_str = b"2FwFnT"
    print(base58.b58decode(test_str))


test_base58()
