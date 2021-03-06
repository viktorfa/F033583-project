import operator

import time

import datetime
from scipy.spatial.distance import cdist

from common.io import load_song_objects
from indexer.inverted_index import IndexProvider
from retrieval.ranker import Ranker
from retrieval import search_log


class Retriever:
    """
    The Retriever is the class handling string queries from the server and returns a usable result in the form of a Query.
    """

    def __init__(self,
                 index_fields=list([
                     ['title'],
                     ['lyrics'],
                     ['artist'],
                     ['artist', 'lyrics'],
                     ['artist', 'title'],
                     ['title', 'lyrics'],
                     ['title', 'lyrics', 'artist']
                 ]),
                 scraper_output_file='example_output.json'
                 ):
        self.index_provider = IndexProvider(scraper_output_file)

        self.indices = {'default': self.index_provider.get_inverted_index(['title'])}

        for field in index_fields:
            self.indices[str(sorted(field))] = self.index_provider.get_inverted_index(field)

        self.song_objects = load_song_objects(scraper_output_file)
        self.song_objects_dict = {int(song_object['id']): song_object for song_object in self.song_objects}

    def retrieve(self, query, filters=list([]), index='default', ranker=Ranker()):
        if type(index) is list:
            index = str(sorted(index))
        query = Query(query, self.indices[index], self.song_objects_dict, self, ranker=ranker, filters=filters)
        query_id = search_log.register_query(query)
        query.execute_query(query_id)

        return query

    def print_results(self, query, sorted_ranking, index):
        print("Results for '{}' over index '{}':".format(query, index))
        for document_id, score in sorted_ranking:
            print(document_id, self.song_objects[document_id]['title'], score)


class Query:
    """
    A Query starts its lifecycle with a query string and some context data. It then works as a wrapper for ranking, 
    filtering and sorting results from that query.
    """

    def __init__(self, query, index, song_objects_dict, retriever, ranker=Ranker(), filters=list([])):
        self.query = query
        self.index = index
        self.song_objects_dict = song_objects_dict
        self.ranker = ranker
        self.retriever = retriever
        self.filter_functions = filters
        self.relevance_ranking_dict = None
        self.sorted_relevance_ranking = None
        self.filtered_ids = None
        self.ranking_dict = None
        self.query_id = None
        self.results = None
        self.start_time = datetime.datetime.now()
        self.processing_time = None

    def execute_query(self, query_id=None):
        query_matrix = self.index.get_query_matrix(self.query)

        distances = cdist(query_matrix.todense(), self.index.get_matrix().todense(), metric='cosine')[0]
        self.relevance_ranking_dict = {document_id: score for document_id, score in enumerate(distances)}
        self.sorted_relevance_ranking = sorted(
            [(document_id, score,) for document_id, score in self.relevance_ranking_dict.items()],
            key=operator.itemgetter(1))

        self.filter_irrelevant_results()

        self.filter_results()

        self.results = [song_object for document_id, song_object in self.song_objects_dict.items() if
                        document_id in self.filtered_ids]

        self.rank_results()

        self.add_analytics_to_results()

        self.sort_results()

        self.query_id = query_id

        self.processing_time = datetime.datetime.now() - self.start_time

    def rank_results(self):
        self.ranking_dict = self.ranker.get_ranking_dict(self.song_objects_dict, self.relevance_ranking_dict, self)

    def sort_results(self):
        self.results = sorted(self.results, key=lambda x: x['ranking']['score'], reverse=True)

    def add_analytics_to_results(self):
        for song_object in self.results:
            song_object['ranking'] = self.ranking_dict[int(song_object['id'])]

    def filter_irrelevant_results(self):
        self.song_objects_dict = {key: self.song_objects_dict[key] for key, value in self.sorted_relevance_ranking
                                  if value < self.sorted_relevance_ranking[-1][1]}

    def filter_results(self):
        print("Filtering results")
        print(self.filter_functions)
        self.filtered_ids = self.song_objects_dict.keys()
        for filter_function in self.filter_functions:
            self.filtered_ids = [document_id for document_id, value in self.song_objects_dict.items() if
                                 document_id in self.filtered_ids and filter_function(value)]

    def get_sorted_results_with_analytics(self):
        return self.results

    def get_meta_information(self):
        """
        Some useful meta information about the query execution and techniques of the search
        :return: 
        """
        return dict(
            total_songs_in_index=self.index.get_meta_information()['num_documents'],
            total_terms_in_index=self.index.get_meta_information()['num_terms'],
            relevant_songs=len(self.song_objects_dict),
            retrieved_songs=len(self.filtered_ids),
            query=self.query,
            index=self.index.get_fields(),
            query_id=self.query_id,
            query_processing_time=self.processing_time.microseconds / 1000 + self.processing_time.seconds * 1000

        )

    def get_query(self):
        return self.query
