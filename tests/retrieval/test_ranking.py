# -*- coding: utf-8 -*-
import unittest

from retrieval.ranker import Ranker, DateRanker


class TestRanking(unittest.TestCase):
    def setUp(self):
        self.ranking_object_1 = Ranker()
        self.ranking_object_2 = Ranker(relevancy=0, popularity=100)
        self.date_ranker_1 = DateRanker()
        self.song_objects = song_objects
        self.relevancy_ranking = relevancy_ranking

    def test_ranking_simple(self):
        actual = self.ranking_object_1.get_sorted_ranking(self.song_objects, self.relevancy_ranking)
        self.assertIsInstance(actual, list)

    def test_ranking_by_relevancy(self):
        actual = self.ranking_object_1.get_sorted_ranking(self.song_objects, self.relevancy_ranking)

        for rank in range(1, len(actual)):
            self.assertGreaterEqual(actual[rank - 1]['relevance'], actual[rank]['relevance'])

    def test_ranking_by_popularity(self):
        actual = self.ranking_object_2.get_sorted_ranking(self.song_objects, self.relevancy_ranking)

        for rank in range(1, len(actual)):
            self.assertGreaterEqual(actual[rank - 1]['popularity'], actual[rank]['popularity'])

    def test_ranking_by_date(self):
        actual = self.date_ranker_1.get_sorted_ranking(self.song_objects, self.relevancy_ranking)

        for rank in range(1, len(actual)):
            self.assertGreaterEqual(actual[rank - 1]['date'], actual[rank]['date'])


song_objects = [
    {
        'album_rating': 8.0,
        'year_released': 2014,
        'id': 0
    },
    {
        'album_rating': 9.0,
        'year_released': 2013,
        'id': 1
    },
    {
        'album_rating': 9.0,
        'year_released': 2012,
        'id': 2
    },
    {
        'album_rating': 3.0,
        'year_released': 2011,
        'id': 3
    },
    {
        'album_rating': 9.0,
        'year_released': 2010,
        'id': 4
    },
]

relevancy_ranking = [
    (0, 0.1),
    (1, 0.2),
    (2, 0.2),
    (3, 0.1),
    (4, 0.4),
]
