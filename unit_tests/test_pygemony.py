from mock import patch

import unittest

from pyg.Pygemony import Pygemony

class PygemonyTestCase(unittest.TestCase):

    def test_hashing_pass(self):
        md5 = Pygemony.hash_todo("# TODO(ian): Testing 123", 5, 'test.py')
        self.assertEqual(md5, "3ce18a4c1ef5500be307fd49bae6a37e")
