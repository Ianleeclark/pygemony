from mock import patch

import unittest

from pyg.Pygemony import Pygemony

class PygemonyTestCase(unittest.TestCase):

    def test_hashing_pass(self):
        md5 = Pygemony.hash_todo("# TODO(ian): Testing 123")
        self.assertEqual(md5, "8b462bbebbaf3628e4b84b12b9d178af")
