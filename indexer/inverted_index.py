import os
import re
import json
import nltk
from scipy import sparse
from scipy.spatial import distance
from pprint import pprint


def get_inverted_index(fields=list(['title'])):
    file_name = "inverted_index_for_%s.json" % str(fields)
    if file_name in os.listdir('.'):
        with open(file_name, 'r') as input_file:
            return json.load(input_file)
    else:
        return create_inverted_index(fields=fields)


def get_document_matrix(inverted_index, use_sparse=True):
    result = []
    meta_information = inverted_index['meta_information']
    N = meta_information['num_documents']
    for document_id in range(N):
        vector = [value[str(document_id)] if str(document_id) in value.keys() else 0 for key, value in
                  inverted_index.items()]
        result.append(vector)
    if use_sparse:
        return sparse.csr_matrix(result)
    else:
        return sparse.csr_matrix(result).todense()


def tokenize(document):
    document = re.sub(r'[^A-Z^a-z^0-9]', ' ', document)
    return [token.lower() for token in document.split()]


def create_inverted_index(input_file_name='scraper/example_output.json', fields=list(['title'])):
    """
    Creates an inverted index and writes it to a file based on some structured input from the scraper,
    indexed by the specified fields.
    :param input_file_name:
    :param fields:
    :return:
    """
    try:
        with open(input_file_name, 'r') as input_file:
            song_objects = json.load(input_file)
    except FileNotFoundError as e:
        print(e)
        return

    documents = []

    for song in song_objects:
        documents.append(' '.join([value for key, value in song.items() if key in fields]))

    inverted_index = {}

    for document_id, document in enumerate(documents):
        tokens = tokenize(document)
        token_counts = [(token, tokens.count(token),) for token in set(tokens)]
        for token, count in token_counts:
            if token in inverted_index.keys():
                inverted_index[token][document_id] = count
                inverted_index[token]['df'] += 1
            else:
                inverted_index_entry = {
                    document_id: count,
                    'df': 1
                }
                inverted_index[token] = inverted_index_entry

    meta_information = dict(
        num_documents=len(documents),
        num_terms=len(inverted_index),
    )

    inverted_index['meta_information'] = meta_information

    print("Created inverted index for %d objects over fields: %s" % (len(song_objects), str(fields)))
    pprint(meta_information)
    with open('./inverted_index_for_%s.json' % (str(fields)), 'w') as output_file:
        json.dump(inverted_index, output_file)

    return inverted_index
