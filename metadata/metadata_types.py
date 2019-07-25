class FunctionCallArgV5:
    def __init__(self):
        self.name = ''
        self.type = ''


class EventArgV5:
    def __init__(self):
        self.name = ''
        self.args = []
        self.doc = []


class CallV5:
    def __init__(self):
        self.name = ''
        self.args = []  # FunctionCallArgV5
        self.doc = []   # string


class FuncTypeV5:
    def __init__(self):
        self.type = 0
        self.key1 = ''
        self.key2 = ''
        self.value = ''
        self.key2_hasher = ''
        self.is_linked = False


class StorageV5:
    def __init__(self):
        self.name = ''
        self.modifier = ''
        self.type = FuncTypeV5()
        self.fallback = ''
        self.doc = []


class ModuleV5:
    def __init__(self):
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV5
        self.call = []  # CallV5
        self.event = []  # EventArgV5


class MetadataV5:
    def __init__(self):
        self.module = []  # ModuleV5
