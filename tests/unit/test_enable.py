import unittest
import os
import shutil

from nsc import add_static # pylint: disable=import-error
from nsc import enable # pylint: disable=import-error

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

class TestAdd(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

    def test_add(self):
        path = "/etc/nginx/sites-enabled/example.com.conf"
        add_static("example.com")
        self.assertFalse(os.path.exists(path))
        enable("example.com")

        self.assertTrue(os.path.exists(path))

    def test_long_add(self):
        path = "/etc/nginx/sites-enabled/asonetuhasonetuhasonetuh.conf"
        add_static("asonetuhasonetuhasonetuh")
        self.assertFalse(os.path.exists(path))
        enable("asonetuhasonetuhasonetuh")
        self.assertTrue(os.path.exists(path))

    def test_short_add(self):
        path = "/etc/nginx/sites-enabled/a.conf"
        add_static("a")
        self.assertFalse(os.path.exists(path))
        enable("a")
        self.assertTrue(os.path.exists(path))

    def test_two_add(self):
        path = "/etc/nginx/sites-enabled/example.com.conf"
        path2 = "/etc/nginx/sites-enabled/test.com.conf"
        add_static("example.com")
        add_static("test.com")
        self.assertFalse(os.path.exists(path))
        self.assertFalse(os.path.exists(path2))
        enable("example.com")
        enable("test.com")
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.exists(path2))

