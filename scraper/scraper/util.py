# -*- coding: utf-8 -*-


def process_artist_links(links):
    print(links)
    for link in links:
        splitted_url = link.url.split('/')
        artist_id = splitted_url[-1]
        link.url = '/'.join(splitted_url[0:-1]) + '/top-' + artist_id
    return links
