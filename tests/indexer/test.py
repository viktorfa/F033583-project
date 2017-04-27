# -*- coding: utf-8 -*-
import unittest

from indexer.inverted_index import tokenize


class TestInvertedIndex(unittest.TestCase):
    def setUp(self):
        pass

    def test_tokenize_simple(self):
        document = 'Take me to the top'
        actual = tokenize(document)

        self.assertIsInstance(actual, list)
        self.assertGreater(len(actual), 0)

    def test_get_inverted_index_simple(self):
        pass
