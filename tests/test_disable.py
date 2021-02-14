import unittest
import os
import shutil

from nsc import disable # pylint: disable=import-error

def clean_files():
    paths = []
    paths.append('/etc/nginx/sites-enabled/')
    for path in paths:
        for root, dirs, files in os.walk(path):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

class TestDisable(unittest.TestCase):

    def tearDown(self):
        clean_files()

    def setUp(self):
        clean_files()

    def test_disable(self):
        conf = "/etc/nginx/sites-enabled/example.com.conf"
        os.mknod(conf)

        disable("example.com")

        self.assertFalse(os.path.exists(conf))




