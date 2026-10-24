from abc import ABC, abstractmethod
import os


class BaseType(ABC):
    value = None

    def _read_value(self, name, prefix, data=None):
        var_name = name.upper()
        if prefix != "":
            var_name = f"{prefix}_{var_name}"

        env_value = os.environ.get(var_name)

        if env_value != None:
            return env_value

        if data != None:
            return data

        return None

    @abstractmethod
    def parse(self, name, prefix, data=None):
        pass


class String(BaseType):
    def __init__(self, data=None):
        self.value = ""

    def parse(self, name, prefix, data=None):
        self.value = str(self._read_value(name, prefix, data))

    def __str__(self) -> str:
        return self.value


class Dict(BaseType):
    def __init__(self, default=None):
        self.value = {}

    def parse(self, name, prefix, data=None):
        prefix = f"{prefix}_{name.upper()}" if prefix != "" else name.upper()

        for key in dir(self):
            cur_key_data = None
            if data != None and key in data:
                cur_key_data = data[key]

            if not isinstance(getattr(self, key), BaseType):
                continue

            getattr(self, key).parse(key, prefix, cur_key_data)
