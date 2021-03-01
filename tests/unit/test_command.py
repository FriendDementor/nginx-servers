import subprocess
import unittest
import shutil
import os

def execute(command):
    result = subprocess.check_output(command.split())
    return result.decode("utf-8")

def clean_files():
    paths = []
    paths.append('/html/')
    paths.append('/etc/nginx/sites-available/')
    paths.append('/etc/nginx/sites-enabled/')
    for path in paths:
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

    execute("nginx -s reload")

class TestShellCommand(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

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

    def test_add_delete(self):
        result = execute("nsc add taka")
        self.assertEqual(result, "OK\n")
        result = execute("nsc add taka")
        self.assertEqual(result, "ERROR\n")
        result = execute("nsc delete taka")
        self.assertEqual(result, "OK\n")
        result = execute("nsc delete taka")
        self.assertEqual(result, "ERROR\n")

