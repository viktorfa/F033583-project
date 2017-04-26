import re
from scipy import sparse
from pprint import pprint

from common.io import load_inverted_index, load_song_objects, write_inverted_index


def get_inverted_index(fields=list(['title'])):
    existing_inverted_index = load_inverted_index(fields)
    if existing_inverted_index:
        return existing_inverted_index
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


def create_inverted_index(input_file_name='example_output.json', fields=list(['title'])):
    """
    Creates an inverted index and writes it to a file based on some structured input from the scraper,
    indexed by the specified fields.
    :param input_file_name:
    :param fields:
    :return:
    """
    try:
        song_objects = load_song_objects(input_file_name)
    except FileNotFoundError as e:
        print(e)
        return

    documents = []

    for song in song_objects:
        documents.append(' '.join([value if key in fields else ' ' for key, value in song.items()]))

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

    write_inverted_index(fields, inverted_index)

    return inverted_index
