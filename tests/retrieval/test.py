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
        self.assertIsInstance(actual, csr_matrix)


class TestRetriever(unittest.TestCase):
    def setUp(self):
        self.retriever_1 = Retriever()

    def test_retrieve_simple(self):
        query = 'bad girl'
        actual = self.retriever_1.retrieve(query)

        self.assertIsNotNone(actual)

    def test_retrieve_by_multiple_fields(self):
        index_fields = [['title', 'lyrics', 'artist']]
        retriever = Retriever(index_fields)
        query = 'you are my bad girl'
        actual = retriever.retrieve(query, index=str(index_fields[0]))

        self.assertIsNotNone(actual)
