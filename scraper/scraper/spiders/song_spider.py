# -*- coding: utf-8 -*-
from scrapy import Request
from datetime import datetime

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.loaders import SongLoader
from scraper.util import process_artist_links


class SongSpider(CrawlSpider):
    allowed_domains = ['www.xiami.com']
    name = 'song_spider'
    start_urls = ['http://www.xiami.com/genre/detail/gid/1']

    rules = [
        Rule(
            LinkExtractor(
                allow=('/artist/\w+',)
            ),
            follow=True,
            process_links=process_artist_links
        ),
        Rule(
            LinkExtractor(
                allow=('/song/\w+',)
            ),
            callback='parse_song_url'
        ),
    ]

    def parse_song_url(self, response):
        song_loader = SongLoader(response=response)
        album_url = response.xpath('//table[@id="albums_info"]//a[contains(@href, "album")]/@href').extract()

        if album_url:
            album_url = album_url[0]
        else:
            return song_loader.load_item()

        song_loader.add_css('title', '#title h1::text')
        song_loader.add_xpath(
            'artist',
            '//table[@id="albums_info"]//tr/td[contains(text(), "演唱者")]/following-sibling::td/div/a/text()'
        )
        song_loader.add_xpath(
            'co_artists',
            '//table[@id="albums_info"]//tr/td[contains(text(), "演唱者")]/following-sibling::td/div/a/text()'
        )
        song_loader.add_xpath(
            'song_writers',
            '//table[@id="albums_info"]//tr/td[contains(text(), "作词")]/following-sibling::td/div/text()'
        )
        song_loader.add_xpath(
            'composers',
            '//table[@id="albums_info"]//tr/td[contains(text(), "作曲")]/following-sibling::td/div/text()'
        )
        song_loader.add_xpath(
            'arrangers',
            '//table[@id="albums_info"]//tr/td[contains(text(), "编曲")]/following-sibling::td/div/text()'
        )
        song_loader.add_value('source_url', response.url)
        song_loader.add_css('lyrics', '#lrc .lrc_main')
        song_loader.add_value('timestamp', str(datetime.utcnow()))

        music_counts = response.css('div.music_counts ul li').extract()

        # song_loader.add_value('num_listens', music_counts[0]) Need to load JS
        song_loader.add_value('num_shares', music_counts[1])
        song_loader.add_value('num_comments', music_counts[2])

        yield Request(response.urljoin(album_url), callback=self.parse_album_url, meta=dict(loader=song_loader))

    def parse_album_url(self, response):
        song_loader = response.meta['loader']
        song_loader.selector = response.css('body')

        song_loader.add_xpath('year_released', '//div[@id="album_info"]//td[contains(text(), "年")]/text()')
        song_loader.add_xpath('record_label', '//div[@id="album_info"]//td/a[contains(@href, "company")]/text()')
        song_loader.add_xpath('genres', '//div[@id="album_info"]//td/a[contains(@href, "genre")]/text()')
        song_loader.add_xpath('language', '//div[@id="album_info"]//td/a[contains(text(), "语")]/text()')
        song_loader.add_css('album_rating', 'div#album_rank p em::text')

        yield song_loader.load_item()
