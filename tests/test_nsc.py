import unittest

from nsc import sites # pylint: disable=import-error

class TestNsc(unittest.TestCase):
    def test_usage(self):
        self.assertEqual(sites(), "list of domains")
