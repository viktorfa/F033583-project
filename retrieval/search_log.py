class SearchLog:
    def __init__(self):
        self.query_log = {}
        self.id_count = 0
        self.query_index = {}

    def register_click(self, query_id, song_id):
        self.query_log[query_id].register_click(song_id)

    def register_play(self, query_id, song_id):
        self.query_log[query_id].register_play(song_id)

    def register_query(self, query):
        query_id = self._get_query_id()
        search_log_query = SearchLogQuery(query, query_id)
        self.query_log[query_id] = search_log_query

        if query.get_query() in self.query_index.keys():
            self.query_index[query.get_query()].append(search_log_query)
        else:
            self.query_index[query.get_query()] = [search_log_query]
        return query_id

    def get_songs_clicked_for_query(self, query):
        result = []
        if query not in self.query_index.keys():
            return result
        else:
            for search_log_query in self.query_index[query]:
                result.extend(search_log_query.get_songs_clicked())

        return result

    def get_songs_played_for_query(self, query):
        result = []
        if query not in self.query_index.keys():
            return result
        else:
            for search_log_query in self.query_index[query]:
                result.extend(search_log_query.get_songs_played())

        return result

    def _get_query_id(self):
        temp = self.id_count
        self.id_count += 1
        return temp


class SearchLogQuery:
    def __init__(self, query, query_id):
        self.query = query
        self.query_id = query_id
        self.songs_clicked = []
        self.songs_played = []

    def register_click(self, song_id):
        self.songs_clicked.append(song_id)

    def register_play(self, song_id):
        self.songs_clicked.append(song_id)

    def get_songs_clicked(self):
        return [x for x in self.songs_clicked]

    def get_songs_played(self):
        return [x for x in self.songs_played]
