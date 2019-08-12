from substrate_python_api.tests.config import async_call


extrinsic = '0x0123456789'

commands = [("state_getMetadata", []),
            ("state_getRuntimeVersion", []),
            ]


for command, parameter in commands:
    async_call(command, parameter)

