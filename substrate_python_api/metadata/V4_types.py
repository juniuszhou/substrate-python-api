class FunctionCallArgV4:
    def __init__(self):
        self.name = ''
        self.type = ''


class EventArgV4:
    def __init__(self):
        self.name = ''
        self.args = []
        self.doc = []


class CallV4:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.args = []  # FunctionCallArgV4
        self.doc = []  # string


class FuncTypeV4:
    def __init__(self):
        self.type = 0
        self.key1 = ''
        self.key2 = ''
        self.value = ''
        self.key2_hasher = ''
        self.is_linked = False


class StorageV4:
    def __init__(self):
        self.name = ''
        self.modifier = ''
        self.type = FuncTypeV4()
        self.fallback = ''
        self.doc = []


class ModuleV4:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV4
        self.call = []  # CallV4
        self.event = []  # EventArgV4


class ModuleV4:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV4
        self.call = []  # CallV4
        self.event = []  # EventArgV4
        self.const = []


class ConstV4:
    def __init__(self):
        self.name = ''
        self.type = ''  # FunctionCallArgV4
        self.value = ''
        self.doc = []  # string


class ConstV4:
    def __init__(self):
        self.name = ''
        self.type = ''  # FunctionCallArgV4
        self.value = ''
        self.doc = []  # string


class MetadataV4:
    def __init__(self):
        self.module = []  # ModuleV4
