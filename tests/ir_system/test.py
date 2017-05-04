# -*- coding: utf-8 -*-
import unittest

from retrieval.retrieval import Retriever, Query
from retrieval.util import parse_filters, parse_ranking


class TestRetrievalSimulation(unittest.TestCase):
    def setUp(self):
        self.retriever = Retriever()

    def validate_retrieval(self, query, query_object):
        self.assertIsInstance(query_object, Query)
        self.assertEqual(query, query_object.get_query())

        results = query_object.get_sorted_results_with_analytics()
        query_meta = query_object.get_meta_information()

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        self.assertIsInstance(query_meta, dict)

        self.assertEqual(len(query_object.song_objects_dict), query_meta['total_songs'])
        self.assertEqual(len(results), query_meta['retrieved_songs'])
        self.assertEqual(query, query_meta['query'])

        # test if ranking is done correctly
        for i in range(1, len(results)):
            self.assertGreaterEqual(results[i - 1]['ranking']['score'], results[i]['ranking']['score'])

    def test_make_query_basic(self):
        query = 'bad girl'
        query_object = self.retriever.retrieve(query)

        self.validate_retrieval(query, query_object)

    def test_make_query_with_filter(self):
        query = 'bad girl'
        filters_string = 'year_released:eq:2010,album_rating:lte:9.2'
        query_object = self.retriever.retrieve(query, filters=parse_filters(filters_string))

        self.validate_retrieval(query, query_object)

        for result in query_object.get_sorted_results_with_analytics():
            self.assertLessEqual(result['album_rating'], 9.2)
            self.assertEqual(result['year_released'], 2010)

    def test_make_query_with_ranking(self):
        query = 'bad girl'
        ranking_string = 'popularity'
        query_object = self.retriever.retrieve(query, ranker=parse_ranking(ranking_string))

        self.validate_retrieval(query, query_object)

        results = query_object.get_sorted_results_with_analytics()

        for i in range(1, len(results)):
            self.assertGreaterEqual(results[i - 1]['ranking']['popularity'], results[i]['ranking']['popularity'])


class TestClickSimulation(unittest.TestCase):
    def setUp(self):
        pass
