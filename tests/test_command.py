import subprocess
import unittest

class TestShellCommand(unittest.TestCase):
    def test_nsc_usage(self):
        result = subprocess.check_output(["nsc"])
        result = str(result)
        self.assertNotEqual(result.find("usage:"), -1)
        self.assertNotEqual(result.find("nsc"), -1)
        self.assertNotEqual(result.find("optional arguments:"), -1)
        self.assertNotEqual(result.find("positional arguments:"), -1)
        self.assertNotEqual(result.find("list"), -1)

    def test_nsc_list(self):
        result = subprocess.check_output(["nsc", "list"])
        result = str(result)
        self.assertEqual(result.find("usage:"), -1)
        self.assertNotEqual(result.find("sites enabled:"), -1)
        self.assertNotEqual(result.find("sites available:"), -1)

