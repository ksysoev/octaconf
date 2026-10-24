from abc import ABC, abstractmethod
import os


class BaseType(ABC):
    value = None

    def parse(self, name, prefix, file=None):
        if file != None:
            pass

        var_name = name.upper()
        if prefix != "":
            var_name = f"{prefix}_{var_name}"

        env_value = os.environ.get(var_name)

        if env_value != None:
            self._parse(env_value)

    @abstractmethod
    def _parse(self, value):
        pass


class String(BaseType):
    def __init__(self, default=None):
        self.value = ""

    def _parse(self, value):
        self.value = str(value)

    def __str__(self) -> str:
        return self.value


class Int(BaseType):
    def __init__(self, default=None):
        self.value = 0

    def _parse(self, value):
        self.value = int(value)

    def __str__(self) -> str:
        return str(self.value)
