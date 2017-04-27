# -*- coding: utf-8 -*-
import unittest

from retrieval.retrieval import Retriever


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_weighted_document_matrix_simple(self):
        pass

    def test_get_weighted_query_matrix(self):
        query = 'Take me to the top'
        pass


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
