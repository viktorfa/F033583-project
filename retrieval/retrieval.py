import math
import operator
from scipy import sparse
from scipy.spatial.distance import cdist

from indexer.inverted_index import get_inverted_index, tokenize


class Retriever:
    def __init__(self):
        self.inverted_indices = {}
        self.inverted_indices['default'] = get_inverted_index()
        self.weighted_matrices = {}
        self.weighted_matrices['default'] = get_weighted_document_matrix(self.inverted_indices['default'])

    def retrieve(self, query, limit=10, filters=None):
        query_matrix = get_weighted_query_matrix(query, self.inverted_indices['default'])

        distances = cdist(query_matrix.todense(), self.weighted_matrices['default'].todense(), metric='cosine')[0]

        print(distances)

        ranking = [(document_id, score,) for document_id, score in enumerate(distances)]
        sorted_ranking = sorted(ranking, key=operator.itemgetter(1), reverse=False)

        return sorted_ranking[:limit]


def get_weighted_document_matrix(inverted_index, weighing='tf_idf'):
    meta_information = inverted_index['meta_information']
    inverted_index = {key: value for key, value in inverted_index.items() if key != 'meta_information'}
    result = []
    N = meta_information['num_documents']
    for document_id in range(N):
        vector = [get_term_weight(value, str(document_id), N) for key, value in inverted_index.items()]
        result.append(vector)
    return sparse.csr_matrix(result)


def get_weighted_query_matrix(query, inverted_index, weighing='tf_idf'):
    meta_information = inverted_index['meta_information']
    inverted_index = {key: value for key, value in inverted_index.items() if key != 'meta_information'}
    N = meta_information['num_documents']

    tokenized_query = tokenize(query)

    vector = [get_query_term_weight(value, tokenized_query.count(key), N) for key, value in inverted_index.items()]

    return sparse.csr_matrix([vector])


def get_query_term_weight(ii_entry, query_term_count, N):
    return tf_idf(query_term_count, ii_entry['df'], N)


def get_term_weight(ii_entry, document_id, N):
    return tf_idf(ii_entry[document_id] if document_id in ii_entry.keys() else 0, ii_entry['df'], N)


def tf_idf(tf, df, N):
    tf = tf
    idf = math.log(1 + N / df, 2)
    return 0.00001 + tf * idf
