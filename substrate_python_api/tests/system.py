from substrate_python_api.tests.config import async_call


commands = [
    'system_name',
    'system_version',
    'system_chain',
    'system_properties',
    'system_health',
    'system_peers',
    'system_networkState'
]


for command in commands:
    async_call(command)
