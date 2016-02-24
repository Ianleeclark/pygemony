from mock import patch

import unittest

from pyg.Pygemony import Pygemony

class PygemonyTestCase(unittest.TestCase):

    def test_hashing_pass(self):
        md5 = Pygemony.hash_todo("# TODO(ian): Testing 123", 'test.py')
        self.assertEqual(md5, "8f83bdfe5ce85ac91d3e84e879fce24e")
