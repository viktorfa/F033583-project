# -*- coding: utf-8 -*-


def process_artist_links(links):
    """
    The LinkExtractor in the spider finds links for artist pages, and this function modifies the links so that the url
    is for the top songs of the artist, because that page contains more song entries.
    :param links:
    :return:
    """
    for link in links:
        splitted_url = link.url.split('/')
        artist_id = splitted_url[-1]
        link.url = '/'.join(splitted_url[0:-1]) + '/top-' + artist_id
    return links
