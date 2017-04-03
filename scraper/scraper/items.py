# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Song(scrapy.Item):
    """
    Defines the fields in the Song item which the scraper populates and finally outputs.
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(serializer=str)
    artist = scrapy.Field(serializer=str)
    co_artists = scrapy.Field(serializer=list)
    lyrics = scrapy.Field(serializer=str)
    song_writers = scrapy.Field(serializer=list)
    composers = scrapy.Field(serializer=list)
    arrangers = scrapy.Field(serializer=list)
    num_listens = scrapy.Field(serializer=int)
    num_shares = scrapy.Field(serializer=int)
    num_comments = scrapy.Field(serializer=int)

    genres = scrapy.Field(serializer=list)
    record_label = scrapy.Field(serializer=str)
    year_released = scrapy.Field(serializer=int)
    language = scrapy.Field(serializer=str)
    album_rating = scrapy.Field(serializer=float)

    source_url = scrapy.Field(serializer=str)
    id = scrapy.Field(serializer=str)
    timestamp = scrapy.Field(serializer=str)
