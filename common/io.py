import json
import os

from common import constants


def load_song_objects(input_file_name):
    path = os.path.join(constants.SCRAPER_OUTPUT_FOLDER, input_file_name)
    with open(path, 'r') as input_file:
        return json.load(input_file)


def load_inverted_index(scraper_output_file_name, fields):
    file_name = "%s/inverted_index_for_%s.json" % (remove_file_type_suffix(scraper_output_file_name), str(fields))
    if file_name in os.listdir(constants.INVERTED_INDEX_FOLDER):
        with open(os.path.join(constants.INVERTED_INDEX_FOLDER, file_name), 'r') as input_file:
            return json.load(input_file)
    else:
        return None


def write_inverted_index(scraper_output_file_name, index):
    with open(
            os.path.join(constants.INVERTED_INDEX_FOLDER,
                         '%s/inverted_index_for_%s.json' % (
                                 remove_file_type_suffix(scraper_output_file_name), str(index.get_fields()))),
            'w') as output_file:
        json.dump(index.get_inverted_index_for_file(), output_file)


def remove_file_type_suffix(filename):
    if len(filename[1:].rsplit('.')) > 1:
        return filename.rsplit('.', 1)[0]
    else:
        return filename
