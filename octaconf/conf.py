import yaml

from abc import ABC

from . import types


class Config(ABC):
    def parse(self, file_path=None):
        data = None
        if file_path != None:
            with open(file_path) as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)

        for key in dir(self):
            cur_key_data = None
            if data != None and key in data:
                cur_key_data = data[key]

            if not isinstance(getattr(self, key), types.BaseType):
                continue

            getattr(self, key).parse(key, "", cur_key_data)
