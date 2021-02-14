import subprocess
import unittest
import shutil
import os
import re

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

class TestFunctionsHappyPath(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

    def test_nsc_simple_add_web(self):
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 0)

        result = execute("nsc add example.com")
        self.assertEqual(result, "OK\n")

        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 1)

        result = execute("nsc enable example.com")
        self.assertEqual(result, "OK\n")

        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 2)

        result = execute("nsc disable example.com")
        self.assertEqual(result, "OK\n")

        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 1)

        result = execute("nsc delete example.com")
        self.assertEqual(result, "OK\n")

        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 0)

    def test_nsc_add_two_webs(self):
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 0)

        result = execute("nsc add example.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 1)

        result = execute("nsc add test.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("test.com", result)), 1)

        result = execute("nsc enable example.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 2)

        result = execute("nsc enable test.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("test.com", result)), 2)

        result = execute("nsc disable example.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 1)

        result = execute("nsc disable test.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("test.com", result)), 1)

        result = execute("nsc delete example.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("example.com", result)), 0)

        result = execute("nsc delete test.com")
        self.assertEqual(result, "OK\n")
        result = execute("nsc list")
        self.assertEqual(len(re.findall("test.com", result)), 0)

