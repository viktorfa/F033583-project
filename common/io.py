import json
import os

from common import constants


def load_song_objects(input_file_name):
    path = os.path.join(constants.SCRAPER_OUTPUT_FOLDER, input_file_name)
    with open(path, 'r') as input_file:
        return json.load(input_file)


def load_inverted_index(scraper_output_file_name, fields):
    file_name = "inverted_index_for_%s.json" % (str(fields))
    if remove_file_type_suffix(scraper_output_file_name) in os.listdir(constants.INVERTED_INDEX_FOLDER) and \
                    file_name in os.listdir(
                os.path.join(constants.INVERTED_INDEX_FOLDER, remove_file_type_suffix(scraper_output_file_name))):
        with open(os.path.join(
                constants.INVERTED_INDEX_FOLDER,
                remove_file_type_suffix(scraper_output_file_name),
                file_name
        ), 'r') as input_file:
            return json.load(input_file)
    else:
        print("ReturningNone")
        return None


def write_inverted_index(scraper_output_file_name, index):
    file_name = 'inverted_index_for_%s.json' % (str(index.get_fields()))
    path = os.path.join(constants.INVERTED_INDEX_FOLDER, remove_file_type_suffix(scraper_output_file_name), file_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as output_file:
        json.dump(index.get_inverted_index_for_file(), output_file)


def remove_file_type_suffix(file_name):
    if len(file_name[1:].rsplit('.')) > 1:
        return file_name.rsplit('.', 1)[0]
    else:
        return file_name
