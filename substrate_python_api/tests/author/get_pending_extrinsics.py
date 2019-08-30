from substrate_python_api.tests.config import async_call


def print_pending_extrinsic(data):
    print(data)


async_call("author_pendingExtrinsics", [], print_pending_extrinsic, debug=True)

