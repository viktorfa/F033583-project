import unittest

from retrieval.util import parse_filters


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_filters(self):
        filters_string = 'year_released:eq:2010,album_rating:lte:9.2'

        actual = parse_filters(filters_string)

        self.assertIsInstance(actual, list)
        self.assertEqual(len(actual), 2)
        for filter_function in actual:
            self.assertTrue(callable(filter_function))

        song_object_1 = dict(
            year_released=2010,
            album_rating=9.0
        )
        song_object_2 = dict(
            year_released=2011,
            album_rating=10.0
        )

        self.assertTrue(actual[0](song_object_1))
        self.assertTrue(actual[1](song_object_1))

        self.assertFalse(actual[0](song_object_2))
        self.assertFalse(actual[1](song_object_2))
