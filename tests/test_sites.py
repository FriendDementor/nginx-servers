import unittest
import os
import glob

import sites

FIRST_TITLE = "sites available:"
SECOND_TITLE = "sites enabled:"

BASE_PATH = "/etc/nginx/"

SITES_AVAILABLE_PATH = BASE_PATH + "sites-available/"
SITES_ENABLED_PATH = BASE_PATH + "sites-enabled/"

class TestSites(unittest.TestCase):

    def tearDown(self):
        files = glob.glob(SITES_AVAILABLE_PATH + '*')
        for f in files:
            os.remove(f)
        files = glob.glob(SITES_ENABLED_PATH + '*')
        for f in files:
            os.remove(f)

    def test_empty(self):
        expected = FIRST_TITLE + "\n\n" + SECOND_TITLE + "\n\n"
        self.assertEqual(sites(), expected)

    def test_one_available(self):
        with open(SITES_AVAILABLE_PATH + 'example.com.conf', 'w') as _: pass
        expected = "sites available:\nexample.com\n\nsites enabled:\n\n"
        self.assertEqual(sites(), expected)

    def test_some_available(self):
        with open(SITES_AVAILABLE_PATH + 'example.com.conf', 'w') as _: pass
        with open(SITES_AVAILABLE_PATH + 'test.com.conf', 'w') as _: pass
        expected = "sites available:\nexample.com\ntest.com\n\nsites enabled:\n\n"
        self.assertEqual(sites(), expected)

    def test_one_enable(self):
        with open(SITES_ENABLED_PATH + 'example.com.conf', 'w') as _: pass
        expected = "sites available:\n\nsites enabled:\nexample.com\n\n"
        self.assertEqual(sites(), expected)

    def test_some_enable(self):
        with open(SITES_ENABLED_PATH + 'example.com.conf', 'w') as _: pass
        with open(SITES_ENABLED_PATH + 'test.com.conf', 'w') as _: pass
        expected = "sites available:\n\nsites enabled:\nexample.com\ntest.com\n\n"
        self.assertEqual(sites(), expected)

    def test_available_enable(self):
        with open(SITES_AVAILABLE_PATH + 'example.com.conf', 'w') as _: pass
        with open(SITES_ENABLED_PATH + 'test.com.conf', 'w') as _: pass
        expected = "sites available:\nexample.com\n\nsites enabled:\ntest.com\n\n"
        self.assertEqual(sites(), expected)

