# -*- coding: utf-8 -*-
import unittest

from scrapy.link import Link

from scraper.scraper.util import process_artist_links


class TestStaticMethods(unittest.TestCase):
    def setUp(self):
        self.expected_link_urls = ['http://www.xiami.com/artist/top-9Lp4eeb0', 'http://www.xiami.com/artist/top-9Lp4eeb1']
        self.links = [Link(url='http://www.xiami.com/artist/9Lp4eeb0'), Link('http://www.xiami.com/artist/9Lp4eeb1')]

    def test_process_artist_link(self):
        actual_links = process_artist_links(self.links)

        for actual_link, expected_url in zip(actual_links, self.expected_link_urls):
            self.assertEqual(actual_link.url, expected_url)
