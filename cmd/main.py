import os
import sys

module_path = os.path.abspath(os.path.join('.'))
if module_path not in sys.path:
    sys.path.append(module_path)

import argparse
from indexer.inverted_index import IndexProvider

index_fields = [
    ['lyrics'],
    ['title'],
    ['artist'],
    ['artist', 'lyrics'],
    ['artist', 'title'],
    ['title', 'lyrics'],
    ['title', 'lyrics', 'artist']
]
"""
"""

parser = argparse.ArgumentParser('Start indexing scraper output.')

parser.add_argument('pos_arg', type=str,
                    help='File name of the output file from the scraper.')

args = parser.parse_args()

print(args.pos_arg)

ip = IndexProvider(args.pos_arg)

for index in index_fields:
    ip.create_inverted_index(index)
