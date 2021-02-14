import unittest
import os
import shutil

from nsc import add_static # pylint: disable=import-error
from nsc import delete_static # pylint: disable=import-error

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

class TestDelete(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

    def test_delete(self):
        conf = "/etc/nginx/sites-available/example.com.conf"
        html = "/html/example.com/"
        os.mknod(conf)
        os.mkdir(html)
        os.mknod(html+'index.html')

        delete_static("example.com")

        self.assertFalse(os.path.exists(conf))
        self.assertFalse(os.path.exists(html))
        self.assertFalse(os.path.exists(html+'index.html'))



