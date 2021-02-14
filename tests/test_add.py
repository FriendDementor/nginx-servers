import unittest
import os
import shutil

from nsc import add_static # pylint: disable=import-error

def clean_files():
    paths = []
    paths.append('/html/')
    paths.append('/etc/nginx/sites-available/')
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
        conf = "/etc/nginx/sites-available/example.com.conf"
        html = "/html/example.com/index.html"
        self.assertFalse(os.path.exists(conf))
        self.assertFalse(os.path.exists(html))

        add_static("example.com")

        self.assertTrue(os.path.exists(conf))
        self.assertTrue(os.path.exists(html))

    def test_long_and(self):
        conf = "/etc/nginx/sites-available/asonetuhasonetuhasonetuh.conf"
        html = "/html/asonetuhasonetuhasonetuh/index.html"
        self.assertFalse(os.path.exists(conf))
        self.assertFalse(os.path.exists(html))
        add_static("asonetuhasonetuhasonetuh")
        self.assertTrue(os.path.exists(conf))
        self.assertTrue(os.path.exists(html))

    def test_short_and(self):
        conf = "/etc/nginx/sites-available/a.conf"
        html = "/html/a/index.html"
        self.assertFalse(os.path.exists(conf))
        self.assertFalse(os.path.exists(html))
        add_static("a")
        self.assertTrue(os.path.exists(conf))
        self.assertTrue(os.path.exists(html))

    def test_two_add(self):
        conf1 = "/etc/nginx/sites-available/example.com.conf"
        html1 = "/html/example.com/index.html"
        conf2 = "/etc/nginx/sites-available/test.com.conf"
        html2 = "/html/test.com/index.html"
        self.assertFalse(os.path.exists(conf1))
        self.assertFalse(os.path.exists(html1))
        self.assertFalse(os.path.exists(conf2))
        self.assertFalse(os.path.exists(html2))
        add_static("example.com")
        add_static("test.com")
        self.assertTrue(os.path.exists(conf1))
        self.assertTrue(os.path.exists(html1))
        self.assertTrue(os.path.exists(conf2))
        self.assertTrue(os.path.exists(html2))



