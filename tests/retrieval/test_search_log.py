import unittest

from retrieval import search_log


class TestSearchLogBasic(unittest.TestCase):
    def setUp(self):
        pass

    def test_register_query(self):
        id_count = search_log.id_count
        query = 'bad girl'
        query_2 = 'heya'
        query_object = QueryMock(query)
        query_object_2 = QueryMock(query_2)
        query_id = search_log.register_query(query_object)
        query_id_2 = search_log.register_query(query_object_2)
        self.assertEqual(id_count + 2, search_log.id_count)
        self.assertNotEqual(query_id, query_id_2)
        self.assertListEqual(search_log.get_songs_clicked_for_query(query_object), [])
        self.assertListEqual(search_log.get_songs_played_for_query(query_object), [])

    def test_register_click(self):
        song_id = 0
        query = 'bad'
        query_object = QueryMock(query)
        query_object_2 = QueryMock(query)

        query_id = search_log.register_query(query_object)
        query_id_2 = search_log.register_query(query_object_2)

        search_log.register_click(query_id, song_id)
        search_log.register_click(query_id, song_id + 1)
        search_log.register_click(query_id_2, song_id + 2)

        expected = [song_id, song_id + 1, song_id + 2]
        actual = search_log.get_songs_clicked_for_query(query)

        self.assertListEqual(actual, expected)


class QueryMock:
    def __init__(self, query):
        self.query = query

    def get_query(self):
        return self.query
