from sr25519.sr25519 import SR25519_PUBLIC_SIZE, SR25519_SIGNATURE_SIZE
from utils.codec import encode_compact_integer

balances_module_index = 1
transfer_method_index = 1
sign_version = 0x81


class TransferExtrinsic:
    # the size of TransferExtrinsic include
    # Era 1 byte
    # sender 32 bytes
    # receiver
    def __init__(self, secret_seed, nonce, receiver, amount):
        self.nonce = nonce
        self.secret_seed = secret_seed
        self.receiver = receiver
        self.amount = amount



