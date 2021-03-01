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
        hosts_files = open("/etc/hosts", "w")
        hosts_files.write("127.0.0.1 example.com")
        hosts_files.close()
        clean_files()

    def test_nsc_simple_add_web(self):

        result = execute("nsc add example.com")
        self.assertEqual(result, "OK\n")

        result = execute("nsc enable example.com")
        self.assertEqual(result, "OK\n")

        result = subprocess.run(['curl', '-v', 'http://example.com/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = result.stdout.decode("utf-8")

        self.assertTrue("< HTTP/1.1 200 OK" in result)
        self.assertTrue("< Content-Type: text/html" in result)
        self.assertTrue("<title>example.com</title>" in result)
        self.assertTrue("The content of example.com" in result)






