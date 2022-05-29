from main import *
import unittest

class TestAddFuncs(unittest.TestCase):
    def test_add_new_shelf_1(self):
        self.assertEqual(add_new_shelf('1'), None)

    def test_add_new_shelf_2(self):
        self.assertEqual(add_new_shelf('4'), '4')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('123', 'passport', 'Gosha', '78'), '78')