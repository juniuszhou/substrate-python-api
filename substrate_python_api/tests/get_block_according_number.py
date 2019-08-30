from substrate_python_api.tests.config import async_call
import json


class Data:
    block_hash = None


block_number = 925


def get_hash(data):
    header = json.loads(data)
    Data.block_hash = header['result']
    print(Data.block_hash)


async_call("chain_getBlockHash", [block_number], get_hash)


def get_block(data):
    header = json.loads(data)
    Data.block_hash = header['result']
    log = header['result']['block']['header']['digest']['logs']
    print(log)


async_call("chain_getBlock", [Data.block_hash], get_block, debug=True)


"""
"result": {
        "block": {
            "extrinsics": [
                "0x01010003845b595d"
                ## unknown
            ],
            "header": {
                "digest": {
                    "logs": [
                        "0x0661757261205abc550900000000",
                        ## 06617572612 unknown
                        ## Pre runtime engine id aura: 5abc550900000000
                        "0x056175726101010c69ff47b1635932f8b790a291289524d5ec8186b8aac4618a4bb7208a3745c6ff87273ccec5b4eb29abe5b7818b057d5e3a0f825df093c57643c17cb2de7205"
                        ## 05617572610101 unknown
                        ## Seal engine id aura: 
                        0c69ff47b1635932f8b790a291289524d5ec8186b8aac4618a4bb7208a3745c6ff87273ccec5b4eb29abe5b7818b057d5e3a0f825df093c57643c17cb2de7205
                    ]
                },
                "extrinsicsRoot": "0x7e07664e194e0f9dd30eb5d5e6e367889c87078f7131a7822bd6e2a6c651ec24",
                "number": "0x39d",
                "parentHash": "0x800467c9d3d4d95f14e813d7289d73a4ee061761b76f5c17990a49cb7589b64a",
                "stateRoot": "0x404ab7be514b8349b579c816a28fc546a4fae2e8cb464669d927b03d20b27984"
            }
        },
"""
