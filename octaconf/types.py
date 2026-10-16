from abc import ABC, abstractmethod
import os


class BaseType(ABC):
    value = None

    def _parse(self, name, prefix, file=None):
        if file != None:
            pass

        env_value = os.environ.get("_".join([prefix, name.upper()]))

        if env_value != None:
            self.value = env_value

    @abstractmethod
    def parse(self, value):
        pass

    @abstractmethod
    def validate(self):
        pass


class String(BaseType):
    pass
