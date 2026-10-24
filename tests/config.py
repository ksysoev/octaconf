import unittest
from unittest.mock import patch
import os

from octaconf.conf import Config
from octaconf.types import String


class TestConfig(unittest.TestCase):
    def test_parse_env(self):
        expected = "My Test Value"
        mock_env = {"TEST": expected}

        class MyConfig(Config):
            test = String()

        cfg = MyConfig()

        with patch.dict(os.environ, mock_env):
            cfg.parse()

        self.assertEqual(expected, str(cfg.test))


if __name__ == "__main__":
    unittest.main()
