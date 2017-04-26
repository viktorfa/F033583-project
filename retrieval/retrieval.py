import math
import operator
from scipy import sparse
from scipy.spatial.distance import cdist

from common.io import load_song_objects
from indexer.inverted_index import get_inverted_index, tokenize
from retrieval.ranker import Ranker


class Retriever:
    def __init__(self, index_fields=list([['title'], ['lyrics'], ['artist'], ['title', 'lyrics', 'artist']])):
        self.inverted_indices = {}
        self.inverted_indices['default'] = get_inverted_index()
        self.weighted_matrices = {}
        self.weighted_matrices['default'] = get_weighted_document_matrix(self.inverted_indices['default'])

        for field in index_fields:
            self.inverted_indices[str(field)] = get_inverted_index(field)
            self.weighted_matrices[str(field)] = get_weighted_document_matrix(self.inverted_indices[str(field)])

        self.song_objects = load_song_objects()

    def retrieve(self, query, limit=10, filters=None, index='default'):
        query = Query(query, self.inverted_indices[index], self.weighted_matrices[index], self.song_objects)
        query.execute_query()

        self.print_results(query, query.get_relevancy_ranking(), index)
        return query

    def print_results(self, query, sorted_ranking, index):
        print("Results for '{}' over index '{}':".format(query, index))
        for document_id, score in sorted_ranking:
            print(document_id, self.song_objects[document_id]['title'], score)


class Query:
    def __init__(self, query, index, matrix, song_objects, ranker=Ranker()):
        self.query = query
        self.index = index
        self.matrix = matrix
        self.song_objects = song_objects
        self.ranker = ranker
        self.sorted_relevancy_ranking = None
        self.sorted_ranking = None
        self.sorted_results = None

        self.song_objects_dict = {int(song_object['id']): song_object for song_object in song_objects}

    def execute_query(self):
        query_matrix = get_weighted_query_matrix(self.query, self.index)

        distances = cdist(query_matrix.todense(), self.matrix.todense(), metric='cosine')[0]
        relevancy_ranking = [(document_id, score,) for document_id, score in enumerate(distances)]
        self.sorted_relevancy_ranking = sorted(relevancy_ranking, key=operator.itemgetter(1))

        self.rank_results()

        return self.sorted_results

    def rank_results(self):
        self.sorted_ranking = self.ranker.get_sorted_ranking(self.song_objects, self.sorted_relevancy_ranking)
        self.sorted_results = self.ranker.get_ranked_results(self.song_objects_dict, self.sorted_ranking)

    def get_sorted_results(self):
        return self.sorted_results

    def get_ranking(self):
        return self.sorted_ranking

    def get_relevancy_ranking(self):
        return self.sorted_relevancy_ranking


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
