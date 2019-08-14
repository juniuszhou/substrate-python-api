from substrate_python_api.sr25519.sr25519 import SR25519_PUBLIC_SIZE, SR25519_SIGNATURE_SIZE
from substrate_python_api.tests.config import async_call
import json
from substrate_python_api.utils.blake2 import get_blake2_256
import base58
from substrate_python_api.utils.codec import encode_compact_integer

balances_module_index = 5
transfer_method_index = 0
sign_version = 0x81

module_id = 5
method_id = 0
separate = 255

# Alice address.
alice_address = b"5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY"
alice_public_key = base58.b58decode(alice_address)[1:33]

# Bob Address
bob_address = b'5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty'
bob_public_key = base58.b58decode(bob_address)[1:33]


class Extra:
    def __init__(self, era, nonce, weight, fee):
        self.era = era
        self.nonce = nonce
        self.weight = weight
        self.fee = fee

    def build_extra(self):
        # just one byte, byteorder could be little and big.
        era = self.era.to_bytes(1, byteorder='little')
        nonce = encode_compact_integer(self.nonce)
        weight = self.weight.to_bytes(1, byteorder='little')
        fee = self.fee.to_bytes(1, byteorder='little')
        print(era, nonce, weight, fee)
        return era + nonce + weight + fee


class TransferExtrinsic:
    def __init__(self, nonce, amount):
        self.nonce = nonce
        self.amount = amount

    def build_tx(self):
        # compute one by one
        compact_amount = encode_compact_integer(self.amount)
        print('amount length is {}'.format(len(compact_amount)))
        tx_parameter = bob_public_key + compact_amount
        print(tx_parameter)
        data_length = len(tx_parameter)
        data_length += 3  # module id + method id + separator

        data_length += 96  # signature + sender public key

        extra = Extra(1, 2, 0, 0)
        extra_bytes = extra.build_extra()
        data_length += len(extra_bytes)
        signature = b'0' * 64
        print(data_length)

        # add one by one
        tx_data = encode_compact_integer(data_length)
        tx_data += sign_version.to_bytes(1, byteorder='little')
        tx_data += separate.to_bytes(1, byteorder='little')
        tx_data += alice_public_key
        tx_data += signature
        tx_data += extra_bytes
        tx_data += module_id.to_bytes(1, byteorder='little')
        tx_data += method_id.to_bytes(1, byteorder='little')
        tx_data += tx_parameter

        return tx_data



