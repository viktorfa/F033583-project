from pprint import pprint


class Ranker:
    def __init__(self, relevancy=100, popularity=0):
        self.relevancy = relevancy
        self.popularity = popularity

    def get_sorted_ranking(self, song_objects_dict, relevancy_ranking):
        ranking = []
        for document_id, rank in relevancy_ranking:
            rank_object = {
                'id': document_id,
                'relevance': 1 - rank,
                'popularity': get_popularity_score(song_objects_dict[document_id]),
                'date': song_objects_dict[document_id]['year_released']
            }
            ranking.append(rank_object)
        result = sorted(ranking, key=self.get_ranking_function, reverse=True)
        pprint(result)
        return result

    def get_ranked_results(self, song_objects_dict, ranking):
        result = []
        for rank_object in ranking:
            result.append(song_objects_dict[rank_object['id']])
        return result

    def get_ranking_function(self, rank_object):
        return rank_object['relevance'] * self.relevancy + rank_object['popularity'] * self.popularity


class DateRanker(Ranker):
    def __init__(self):
        super().__init__(relevancy=0, popularity=0)

    def get_ranking_function(self, rank_object):
        return rank_object['date']


def get_popularity_score(song_object):
    print(song_object)
    album_rating = song_object['album_rating'] if 'album_rating' in song_object.keys() else 10
    return album_rating / 10  # Should also use other metrics for this


def get_relevant_songs(ranking, song_objects):
    pass
