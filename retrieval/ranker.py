from retrieval import search_log


class Ranker:
    def __init__(self, relevance=100, popularity=0):
        self.relevance = relevance
        self.popularity = popularity

    def get_sorted_ranking(self, song_objects_dict, relevance_ranking):
        ranking = []
        for document_id, rank in relevance_ranking:
            rank_object = {
                'id': document_id,
                'relevance': 1 - rank,
                'popularity': get_popularity_score(song_objects_dict[document_id]),
                'date': song_objects_dict[document_id]['year_released']
            }
            ranking.append(rank_object)
        result = sorted(ranking, key=self.get_ranking_function, reverse=True)
        return result

    def get_ranking_dict(self, song_objects_dict, relevance_ranking_dict, query_object):
        ranking = []
        for document_id, song_object in song_objects_dict.items():
            rank_object = {
                'id': document_id,
                'relevance': 1 - relevance_ranking_dict[document_id],
                'popularity': get_popularity_score(song_objects_dict[document_id]),
                'date': song_objects_dict[document_id]['year_released'] if 'year_released' in song_objects_dict[
                    document_id].keys() else 0,
                'clicks': search_log.get_songs_clicked_for_query(query_object.get_query()).count(document_id)
            }
            rank_object['score'] = self.get_ranking_function(rank_object)
            ranking.append(rank_object)
        return {rank_object['id']: rank_object for rank_object in ranking}

    def get_ranking_function(self, rank_object):
        return rank_object['relevance'] * self.relevance + rank_object['popularity'] * self.popularity + rank_object[
                                                                                                             'clicks'] * 100


class DateRanker(Ranker):
    def __init__(self):
        super().__init__(relevance=0, popularity=0)

    def get_ranking_function(self, rank_object):
        return rank_object['date']


def get_popularity_score(song_object):
    album_rating = song_object['album_rating'] if 'album_rating' in song_object.keys() else 10
    return album_rating / 10  # Should also use other metrics for this
