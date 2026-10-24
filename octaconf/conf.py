from abc import ABC

from . import types


class Config(ABC):
    def parse(self, file=None):
        if file != None:
            pass

        for key in dir(self):
            if not isinstance(getattr(self, key), types.BaseType):
                continue

            getattr(self, key).parse(key, "")
