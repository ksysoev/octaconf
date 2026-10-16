import unittest

from octaconf.conf import Config


class TestConfig(unittest.TestCase):
    def test_parse_env(self):
        Config()


if __name__ == "__main__":
    unittest.main()
