class FunctionCallArgV7:
    def __init__(self):
        self.name = ''
        self.type = ''


class EventArgV7:
    def __init__(self):
        self.name = ''
        self.args = []
        self.doc = []


class CallV7:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.args = []  # FunctionCallArgV7
        self.doc = []  # string


class FuncTypeV7:
    def __init__(self):
        self.type = 0
        self.key1 = ''
        self.key2 = ''
        self.value = ''
        self.key2_hasher = ''
        self.is_linked = False


class StorageV7:
    def __init__(self):
        self.name = ''
        self.modifier = ''
        self.type = FuncTypeV7()
        self.fallback = ''
        self.doc = []


class ModuleV7:
    def __init__(self):
        self.index = 0
        self.name = ''
        self.prefix = ''
        self.storage = []  # StorageV7
        self.call = []  # CallV7
        self.event = []  # EventArgV7
        self.const = []  # ConstV7


class ConstV7:
    def __init__(self):
        self.name = ''
        self.type = ''  # FunctionCallArgV7
        self.value = ''
        self.doc = []  # string



