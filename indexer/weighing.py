import math
import re
from scipy import sparse


class MatrixMaker:
    def __init__(self, weighing='tf-idf'):
        pass

    def get_weighted_document_matrix(self, index):
        meta_information = index.get_meta_information()
        result = []
        N = meta_information['num_documents']
        for document_id in range(N):
            vector = [get_term_weight(value, str(document_id), N) for key, value in index.get_inverted_index().items()]
            result.append(vector)
        return sparse.csr_matrix(result)

    def get_weighted_query_matrix(self, query, index):
        meta_information = index.get_meta_information()
        N = meta_information['num_documents']

        tokenized_query = tokenize(query)

        vector = [get_query_term_weight(value, tokenized_query.count(key), N) for key, value in
                  index.get_inverted_index().items()]

        return sparse.csr_matrix([vector])


def get_query_term_weight(ii_entry, query_term_count, N):
    return tf_idf(query_term_count, ii_entry['df'], N)


def get_term_weight(ii_entry, document_id, N):
    return tf_idf(ii_entry[document_id] if document_id in ii_entry.keys() else 0, ii_entry['df'], N)


def tf_idf(tf, df, N):
    tf = tf
    idf = math.log(1 + N / df, 2)
    return 0.00001 + tf * idf


def tokenize(document):
    document = re.sub(r'[^A-Z^a-z^0-9]', ' ', document)
    return [token.lower() for token in document.split()]
