# -*- coding: utf-8 -*-
import unittest

from scipy.sparse import csr_matrix

from indexer.inverted_index import get_inverted_index
from retrieval.retrieval import get_weighted_document_matrix, get_weighted_query_matrix, Retriever


class Test(unittest.TestCase):
    def setUp(self):
        self.inverted_index_1 = get_inverted_index()

    def test_get_weighted_document_matrix_simple(self):
        actual = get_weighted_document_matrix(self.inverted_index_1)

        self.assertIsInstance(actual, csr_matrix)

    def test_get_weighted_query_matrix(self):
        query = 'Take me to the top'
        actual = get_weighted_query_matrix(query, self.inverted_index_1)
        print(actual)
        self.assertIsInstance(actual, csr_matrix)


class TestRetriever(unittest.TestCase):
    def setUp(self):
        self.retriever_1 = Retriever()

    def test_retrieve_simple(self):
        query = 'bad girl'
        actual = self.retriever_1.retrieve(query)

        print(actual)
