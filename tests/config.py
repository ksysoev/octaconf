import unittest
import os

from unittest.mock import patch

from octaconf.conf import Config
from octaconf.types import String, Dict


class TestConfig(unittest.TestCase):
    def test_parse_string_from_env(self):
        expected = "My Test Value"
        mock_env = {"TEST": expected}

        class MyConfig(Config):
            test = String()

        cfg = MyConfig()

        with patch.dict(os.environ, mock_env):
            cfg.parse()

        self.assertEqual(expected, str(cfg.test))

    def test_parse_dict_from_enb(self):
        expected = "My Test Value"
        mock_env = {"TEST_DICT_KEY": expected}

        class MyDict(Dict):
            key = String()

        class MyConfig(Config):
            test_dict = MyDict()

        cfg = MyConfig()

        with patch.dict(os.environ, mock_env):
            cfg.parse()

        self.assertEqual(expected, str(cfg.test_dict.key))


if __name__ == "__main__":
    unittest.main()
