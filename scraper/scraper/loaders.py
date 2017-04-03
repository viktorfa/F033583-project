# -*- coding: utf-8 -*-
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags

from scraper.items import Song


def parse_int(string):
    matches = re.findall(r'(\d+)', string)

    if matches:
        return matches[0]
    else:
        return None


def parse_float(string):
    matches = re.findall(r'(\d+\.\d+)', string)

    if matches:
        return matches[0]
    else:
        return None


class SongLoader(ItemLoader):
    default_item_class = Song
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    co_artists_out = MapCompose(str.strip)
    song_writers_out = MapCompose(str.strip)
    composers_out = MapCompose(str.strip)
    arrangers_out = MapCompose(str.strip)
    genres_out = MapCompose(remove_tags, str.strip)

    year_released_in = MapCompose(str.strip, lambda x: int(x[:4]))
    lyrics_in = MapCompose(remove_tags, str.strip)
    num_listens_in = MapCompose(remove_tags, parse_int, int)
    num_shares_in = MapCompose(remove_tags, parse_int, int)
    num_comments_in = MapCompose(remove_tags, parse_int, int)
    album_rating_in = MapCompose(remove_tags, parse_float, float)
