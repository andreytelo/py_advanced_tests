from main import *
import unittest

class TestDeleteFuncs(unittest.TestCase):
    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf("11-2"), None)


    def test_move_doc_to_shelf(self):
        self.assertEqual(move_doc_to_shelf('11-2','3'), '3')


    def test_delete_doc_1(self):
        self.assertEqual(delete_doc('11-2'), None)


    def test_delete_doc_2(self):
        self.assertEqual(delete_doc('11-3'), None)