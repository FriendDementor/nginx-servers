import subprocess
import unittest
import shutil
import os
import re
import time

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

class TestFunctionsHappyPath(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        hosts_files = open("/etc/hosts", "w")
        hosts_files.write("127.0.0.1 example.com")
        hosts_files.close()
        clean_files()

    def test_nsc_simple_add_web(self):
        # By default the curl should show a 404
        result = subprocess.run(['curl', '-v', 'http://example.com/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = result.stdout.decode("utf-8")
        self.assertTrue("< HTTP/1.1 404 Not Found" in result)

        # After simply add a templated domain, curl should still show 404
        result = execute("nsc add example.com")
        time.sleep(0.1) # wait a bit time for give time to nginx server to update
        self.assertEqual(result, "OK\n")
        result = subprocess.run(['curl', '-v', 'http://example.com/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = result.stdout.decode("utf-8")
        self.assertTrue("< HTTP/1.1 404 Not Found" in result)

        # Now when enable the domain, curl should works fine
        result = execute("nsc enable example.com")
        time.sleep(0.1) # wait a bit time for give time to nginx server to update
        self.assertEqual(result, "OK\n")
        result = subprocess.run(['curl', '-v', 'http://example.com/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = result.stdout.decode("utf-8")
        self.assertTrue("< HTTP/1.1 200 OK" in result)
        self.assertTrue("< Content-Type: text/html" in result)
        self.assertTrue("<title>example.com</title>" in result)
        self.assertTrue("The content of example.com" in result)

