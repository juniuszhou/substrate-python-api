from substrate_python_api.tests.config import async_call


def print_pending_extrinsic():
    pass


extrinsic_hash = "0x404ab7be514b8349b579c816a28fc546a4fae2e8cb464669d927b03d20b27984"
async_call("author_removeExtrinsic", [(extrinsic_hash, ), ], print_pending_extrinsic(), debug=True)

