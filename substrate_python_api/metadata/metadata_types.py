# from substrate_python_api.metadata.V4_types import ModuleV4
# from substrate_python_api.metadata.V5_types import ModuleV5
# from substrate_python_api.metadata.V6_types import ModuleV6
# from substrate_python_api.metadata.V7_types import ModuleV7


class Metadata:
    def __init__(self):
        self.version = 0
        self.module = []

    def set_version(self, version):
        self.version = version

    def add(self, module):
        self.module.append(module)

