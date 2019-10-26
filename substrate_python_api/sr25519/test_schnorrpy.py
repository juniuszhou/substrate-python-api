import schnorrpy
import binascii
import base64


def test_keypair_from_seed():
    """Test createing a keypair from a 32 byte seed"""
    # seed = hex!("fac7959dbfe72f052e5a0c3c8d6530f202b02fd8f9f5ca3580ec8deb7797479e");
    # expected = hex!("46ebddef8cd9bb167dc30878d7113b7e168e6f0646beffd77d69d39bad76b47a");

    # Define our seed, and comparison data
    hex_string = 'fac7959dbfe72f052e5a0c3c8d6530f202b02fd8f9f5ca3580ec8deb7797479e'
    seed_hex = (
        b'0a8db9cd8fa3c74cfd55839175a255a164d1db2d6fd128efb4ddeec35e29f2ed'
    )
    expected_pub_hex = (
        b'56a1edb23ba39364bca160b3298cfb7ec8c5272af841c59a7160123a7d705c4d'
    )
    expected_private_hex = (b'206882f2fb31a37c64cda4337625ae71ec96f133747c'
                            b'2a79e2d7909825e7d15261236a3191bca4e5ef5fe961'
                            b'4f0403104087d5a39fcfcee40060bdc9b3c19673')
    # unhex our seed value
    seed = binascii.unhexlify(seed_hex)
    print(seed, seed.hex(), len(seed))
    # use schnorrpy to generate our keypair
    keypair = schnorrpy.keypair_from_seed(seed)
    print(binascii.hexlify(keypair[1]), expected_private_hex)
    print(binascii.hexlify(keypair[0]), expected_pub_hex)

    hex_string = 'f0259214683389eef511a08c970cbcd5c692e39a959f9cd31bb5103468a33062'
    seed = bytes(bytearray.fromhex(hex_string))
    keypair = schnorrpy.keypair_from_seed(seed)
    print(binascii.hexlify(keypair[1]), expected_private_hex)
    print(binascii.hexlify(keypair[0]), expected_pub_hex)


test_keypair_from_seed()


# because of a random value, the signature is different each time for same message.
def test_sign():
    """Test that we can successfully sign a message"""
    keypair = (
        binascii.unhexlify(b'56a1edb23ba39364bca160b3298cfb7ec8c5272af841c'
                           b'59a7160123a7d705c4d'),
        # both signature are valid, use different random number.
        # binascii.unhexlify(b'206882f2fb31a37c64cda4337625ae71ec96f133747c'
        #                    b'2a79e2d7909825e7d15261236a3191bca4e5ef5fe961'
        #                    b'4f0403104087d5a39fcfcee40060bdc9b3c19673')
        binascii.unhexlify(b'deabbe56c74e13c4a094b73e4957283a71c812993702e4d'
                           b'2b76dc863e74dea628753a00d9fead732408e33aaeaf695'
                           b'b4830e83e3d3528d4e1d2b8dbce5d4f00d')
    )

    message = base64.b64encode(
        b'it reaches out it reaches out it reaches out it reaches out'
        b'One hundred and thirteen times a second, nothing answers and it'
        b'reaches out. It is not conscious, though parts of it are.'
        b'There are structures within it that were once separate'
        b' organisms; aboriginal, evolved, and complex. It is designed to'
        b' improvise, to use what is there and then move on. Good enough '
        b'is good enough, and so the artifacts are ignored or adapted. '
        b'The conscious parts try to make sense of the reaching out.'
        b'Try to interpret it.')
    sig = schnorrpy.sign(keypair, message)
    print(len(sig), sig.hex())
    print(binascii.unhexlify(b'bcb041916b70af03b17ed1c622817ffa50815499dbe18895d2f9618f006ab'
                             b'64886c69d5a20e04ff66317c7e14d2580dedfc6bbff14c380569cad5c02719c'
                             b'420c'))


test_sign()


def test_verify_valid_signature():
    """Test that we can verify a valid signature"""
    publicKey = binascii.unhexlify(
        b'56a1edb23ba39364bca160b3298cfb7ec8c5272af841c'
        b'59a7160123a7d705c4d')
    sig = binascii.unhexlify(b'bcb041916b70af03b17ed1c622817ffa50815499dbe18895d2f9618f006ab'
                             b'64886c69d5a20e04ff66317c7e14d2580dedfc6bbff14c380569cad5c02719c'
                             b'420c')

    message = base64.b64encode(
        b'it reaches out it reaches out it reaches out it reaches out'
        b'One hundred and thirteen times a second, nothing answers and it'
        b'reaches out. It is not conscious, though parts of it are.'
        b'There are structures within it that were once separate'
        b' organisms; aboriginal, evolved, and complex. It is designed to'
        b' improvise, to use what is there and then move on. Good enough '
        b'is good enough, and so the artifacts are ignored or adapted. '
        b'The conscious parts try to make sense of the reaching out.'
        b'Try to interpret it.')
    print(schnorrpy.verify(sig, message, publicKey))


test_verify_valid_signature()


def test_fail_verify_invalid_signature():
    """Test that a invalid signature will fail to verify"""
    publicKey = binascii.unhexlify(
        b'56a1edb23ba39364bca160b3298cfb7ec8c5272af841c'
        b'59a7160123a7d705c4d')
    sig = binascii.unhexlify(b'bcb041916b70af03b17ed1c622817ffa50815499db'
                             b'e18895d2f9618fdeadbeef86c69d5a20e04ff66317c7e14d2580dedfc6bbff1'
                             b'4c380569cad5c02719c420c')

    message = base64.b64encode(
        b'it reaches out it reaches out it reaches out it reaches out'
        b'One hundred and thirteen times a second, nothing answers and it'
        b'reaches out. It is not conscious, though parts of it are.'
        b'There are structures within it that were once separate'
        b' organisms; aboriginal, evolved, and complex. It is designed to'
        b' improvise, to use what is there and then move on. Good enough '
        b'is good enough, and so the artifacts are ignored or adapted. '
        b'The conscious parts try to make sense of the reaching out.'
        b'Try to interpret it.')
    print(schnorrpy.verify(sig, message, publicKey))
