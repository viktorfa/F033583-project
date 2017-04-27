import json
import os

from common import constants


def load_song_objects(input_file_name='example_output.json'):
    path = os.path.join(constants.SCRAPER_OUTPUT_FOLDER, input_file_name)
    with open(path, 'r') as input_file:
        return json.load(input_file)


def load_inverted_index(fields):
    file_name = "inverted_index_for_%s.json" % str(fields)
    if file_name in os.listdir(constants.INVERTED_INDEX_FOLDER):
        with open(os.path.join(constants.INVERTED_INDEX_FOLDER, file_name), 'r') as input_file:
            return json.load(input_file)
    else:
        return None


def write_inverted_index(index):
    with open(os.path.join(constants.INVERTED_INDEX_FOLDER, './inverted_index_for_%s.json' % (str(index.get_fields()))),
              'w') as output_file:
        json.dump(index.get_inverted_index_for_file(), output_file)
