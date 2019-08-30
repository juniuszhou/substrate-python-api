class FunctionCallArgV6:
    def __init__(self):
        self.name = ''
        self.type = ''


class EventArgV6:
    def __init__(self):
        self.name = ''
        self.args = []
        self.doc = []


class CallV6:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.args = []  # FunctionCallArgV6
        self.doc = []  # string


class FuncTypeV6:
    def __init__(self):
        self.type = 0
        self.key1 = ''
        self.key2 = ''
        self.value = ''
        self.key2_hasher = ''
        self.is_linked = False


class StorageV6:
    def __init__(self):
        self.name = ''
        self.modifier = ''
        self.type = FuncTypeV6()
        self.fallback = ''
        self.doc = []


class ModuleV6:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV6
        self.call = []  # CallV6
        self.event = []  # EventArgV6


class ModuleV6:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV6
        self.call = []  # CallV6
        self.event = []  # EventArgV6
        self.const = []


class ConstV6:
    def __init__(self):
        self.name = ''
        self.type = ''  # FunctionCallArgV6
        self.value = ''
        self.doc = []  # string


class ConstV6:
    def __init__(self):
        self.name = ''
        self.type = ''  # FunctionCallArgV6
        self.value = ''
        self.doc = []  # string


class MetadataV6:
    def __init__(self):
        self.module = []  # ModuleV6
