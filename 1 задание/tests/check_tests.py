from main import *
import unittest


class TestFuncs(unittest.TestCase):
    def test_check_document_existance_1(self):
        self.assertEqual(check_document_existance("2207 876234"), True)

    def test_check_document_existance_2(self):
        self.assertEqual(check_document_existance("22027 876234"), False)

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name("2207 876234"), "Василий Гупкин")

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'})

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('11-2'), '1')

    def test_show_all_docs_info(self):
        self.assertEqual(show_all_docs_info(), [['passport', '2207 876234', 'Василий Гупкин'],
                                                ['invoice', '11-2', 'Геннадий Покемонов'],
                                                ['insurance', '10006', 'Аристарх Павлов']])
