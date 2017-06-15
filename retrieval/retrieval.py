import operator

from copy import deepcopy
from scipy.spatial.distance import cdist

from common.io import load_song_objects
from indexer.inverted_index import IndexProvider
from retrieval.ranker import Ranker
from retrieval import search_log


class Retriever:
    """
    The Retriever is the class handling string queries from the server and returns a usable result in the form of a Query.
    """

    def __init__(self, index_fields=list([
        ['title'],
        ['lyrics'],
        ['artist'],
        ['artist', 'lyrics'],
        ['artist', 'title'],
        ['title', 'lyrics'],
        ['title', 'lyrics', 'artist']
    ])
                 ):
        self.index_provider = IndexProvider()

        self.indices = {}
        self.indices['default'] = self.index_provider.get_inverted_index(['title'])

        for field in index_fields:
            self.indices[str(sorted(field))] = self.index_provider.get_inverted_index(field)

        self.song_objects = load_song_objects()
        self.song_objects_dict = {int(song_object['id']): song_object for song_object in self.song_objects}

    def retrieve(self, query, limit=10, filters=list([]), index='default', ranker=Ranker()):
        if type(index) is list:
            index = str(sorted(index))
        query = Query(query, self.indices[index], self.song_objects_dict, self, ranker=ranker, filters=filters)
        query_id = search_log.register_query(query)
        query.execute_query(query_id)

        # self.print_results(query, query.get_relevancy_ranking(), index)
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
        self.sorted_relevancy_ranking = None
        self.filtered_ids = None
        self.ranking_dict = None
        self.query_id = None

    def execute_query(self, query_id=None):
        query_matrix = self.index.get_query_matrix(self.query)

        distances = cdist(query_matrix.todense(), self.index.get_matrix().todense(), metric='cosine')[0]
        relevancy_ranking = [(document_id, score,) for document_id, score in enumerate(distances)]
        self.sorted_relevancy_ranking = sorted(relevancy_ranking, key=operator.itemgetter(1))

        self.filter_results()
        self.rank_results()

        self.query_id = query_id

    def rank_results(self):
        self.ranking_dict = self.ranker.get_ranking_dict(self.song_objects_dict, self.sorted_relevancy_ranking, self)

    def filter_results(self):
        print("Filtering results")
        print(self.filter_functions)
        self.filtered_ids = self.song_objects_dict.keys()
        for filter_function in self.filter_functions:
            self.filtered_ids = [document_id for document_id, value in self.song_objects_dict.items() if
                                 document_id in self.filtered_ids and filter_function(value)]

    def get_sorted_filtered_results(self):
        return [song_object for document_id, song_object in self.song_objects_dict.items() if
                document_id in self.filtered_ids]

    def get_sorted_results_with_analytics(self):
        result = []
        for song_object in self.get_sorted_filtered_results():
            new_song_object = deepcopy(song_object)
            new_song_object['ranking'] = self.ranking_dict[int(song_object['id'])]
            result.append(new_song_object)
        return sorted(result, key=lambda x: x['ranking']['score'], reverse=True)

    def get_meta_information(self):
        """
        Some useful meta information about the query execution and techniques of the search
        :return: 
        """
        return dict(
            total_songs=len(self.song_objects_dict),
            retrieved_songs=len(self.filtered_ids),
            query=self.query,
            index=self.index.get_fields(),
            query_id=self.query_id
        )

    def get_relevancy_ranking(self):
        return self.sorted_relevancy_ranking

    def get_query(self):
        return self.query
