from substrate_python_api.polkadot.ws.config import async_call


commands = [
    'chain_getFinalizedHead',
    'chain_getBlockHash',
]


for command in commands:
    async_call(command)

