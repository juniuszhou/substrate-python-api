# test sr25519

from substrate_python_api.sr25519.sr25519 import Sr25519
import binascii

def test_generate_from_hex():
    # seed = hex!("fac7959dbfe72f052e5a0c3c8d6530f202b02fd8f9f5ca3580ec8deb7797479e");
    # expected = hex!("46ebddef8cd9bb167dc30878d7113b7e168e6f0646beffd77d69d39bad76b47a");
    sr = Sr25519()
    # seed_bytes = b'fac7959dbfe72f052e5a0c3c8d6530f202b02fd8f9f5ca3580ec8deb7797479e' # doesn't work.
    seed_bytes = bytes.fromhex('0a8db9cd8fa3c74cfd55839175a255a164d1db2d6fd128efb4ddeec35e29f2ed')
    print(seed_bytes)
    private_key, nonce, public_key = sr.sr25519_keypair_from_seed(seed_bytes)
    print(private_key.to_hex(), nonce.to_hex(), public_key.to_hex())
    print(private_key.to_base58(),  public_key.to_base58(), public_key.to_substrate())


def test_generate_from_bytes():
    # seed_hex =  b'0a8db9cd8fa3c74cfd55839175a255a164d1db2d6fd128efb4ddeec35e29f2ed'
    # expected_pub_hex = b'56a1edb23ba39364bca160b3298cfb7ec8c5272af841c59a7160123a7d705c4d'

    sr = Sr25519()

    seed_bytes = b'fac7959dbfe72f052e5a0c3c8d6530f202b02fd8f9f5ca3580ec8deb7797479e'
    seed = binascii.unhexlify(seed_bytes)
    print(seed, len(seed))
    private_key, nonce, public_key = sr.sr25519_keypair_from_seed(seed)
    print(private_key.to_hex(), nonce.to_hex(), public_key.to_hex())
    print(private_key.to_base58(), public_key.to_base58(), public_key.to_substrate())


test_generate_from_bytes()


