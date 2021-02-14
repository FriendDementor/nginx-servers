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

class TestFunctionsHappyPath(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

    def test_nsc_simple_add_web(self):
        # result = execute("nsc list | wc")
        # self.assertEqual(result, "4")
        pass
