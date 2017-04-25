# -*- coding: utf-8 -*-
import unittest

from indexer.inverted_index import tokenize, get_inverted_index


class TestInvertedIndex(unittest.TestCase):
    def setUp(self):
        pass

    def test_tokenize_simple(self):
        document = 'Take me to the top'
        actual = tokenize(document)

        self.assertIsInstance(actual, list)
        self.assertGreater(len(actual), 0)

    def test_get_inverted_index_simple(self):
        actual = get_inverted_index()

        self.assertIsInstance(actual, dict)
        self.assertIn('meta_information', actual.keys())
