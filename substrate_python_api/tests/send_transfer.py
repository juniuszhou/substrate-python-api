from substrate_python_api.tests.config import async_call
import base58
from substrate_python_api.utils.codec import encode_compact_integer

balances_module_index = 5
transfer_method_index = 0
sign_version = 0x82

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

    def build_extra(self):  # 0, 4, 145, 1
        # just one byte, byteorder could be little and big.
        era = self.era.to_bytes(1, byteorder='little')
        nonce = encode_compact_integer(self.nonce)
        weight = self.weight.to_bytes(1, byteorder='little')
        fee = self.fee.to_bytes(1, byteorder='little')
        print(era, nonce, weight, fee)
        # return era + nonce + weight + fee
        return era + nonce + fee


class TransferExtrinsic:
    # the size of TransferExtrinsic include
    # Era 1 byte
    # sender 32 bytes
    # receiver
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

        extra = Extra(0, 2, 0, 0)
        extra_bytes = extra.build_extra()
        data_length += len(extra_bytes)
        signature = b'0' * 64
        print(data_length)

        data_length += 2  # size of sign version and seperate.

        # add one by one
        tx_data = encode_compact_integer(data_length)

        tx_data += sign_version.to_bytes(1, byteorder='little')
        tx_data += separate.to_bytes(1, byteorder='little')
        tx_data += alice_public_key
        tx_data += signature
        tx_data += extra_bytes
        tx_data += module_id.to_bytes(1, byteorder='little')
        tx_data += method_id.to_bytes(1, byteorder='little')
        tx_data += separate.to_bytes(1, byteorder='little')
        tx_data += tx_parameter

        #
        print([x for x in tx_data])
        print(tx_data.hex())
        return '0x' + tx_data.hex()


def deal_with_message(data):
    print(data)


tx = TransferExtrinsic(2, 1)
# print(tx.build_tx())

# data = [41, 2, 130, 255, 48, 100, 193, 176, 231, 2, 44, 71, 100, 223, 13, 233, 226, 216, 238, 23, 128, 72, 196, 14, 60, 177, 152, 59, 104, 182, 55, 167, 209, 143, 22, 96, 24, 84, 229, 197, 112, 142, 183, 91, 38, 224, 184, 23, 132, 171, 228, 230, 122, 140, 192, 38, 154, 239, 161, 159, 156, 55, 0, 18, 221, 172, 17, 107, 218, 135, 4, 0, 105, 194, 60, 244, 220, 111, 61, 33, 110, 54, 90, 49, 54, 190, 144, 84, 111, 50, 164, 195, 72, 173, 197, 42, 38, 223, 92, 6, 0, 4, 145, 1, 5, 0, 255, 48, 100, 193, 176, 231, 2, 44, 71, 100, 223, 13, 233, 226, 216, 238, 23, 128, 72, 196, 14, 60, 177, 152, 59, 104, 182, 55, 167, 209, 143, 22, 96, 4]

data = '0x81ffd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d24aed96956688d3546b35470ec7ff3f4a5b12a7e3dc3d0fa122a53ad80fedf1a4311f68fa42a78401d979aa385c124d71f41e300b74abe88d9d63f2c7b93ff062035000300ff8eaf04151687736326c9fea17e25fc5287613693c912909cb226aa4794f26a48ed01'
# async_call("author_submitExtrinsic", [tx.build_tx()], deal_with_message)
async_call("author_submitExtrinsic", [data,], deal_with_message)
