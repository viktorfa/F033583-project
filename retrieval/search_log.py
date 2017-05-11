id_count = 0
query_log = {}
query_index = {}


def register_click(query_id, song_id):
    query_log[query_id].register_click(song_id)


def register_play(query_id, song_id):
    query_log[query_id].register_play(song_id)


def register_query(query):
    query_id = _get_query_id()
    search_log_query = SearchLogQuery(query, query_id)
    query_log[query_id] = search_log_query

    if query.get_query() in query_index.keys():
        query_index[query.get_query()].append(search_log_query)
    else:
        query_index[query.get_query()] = [search_log_query]
    return query_id


def get_songs_clicked_for_query(query):
    result = []
    if query not in query_index.keys():
        return result
    else:
        for search_log_query in query_index[query]:
            result.extend(search_log_query.get_songs_clicked())

    return result


def get_songs_played_for_query(query):
    result = []
    if query not in query_index.keys():
        return result
    else:
        for search_log_query in query_index[query]:
            result.extend(search_log_query.get_songs_played())

    return result


def _get_query_id():
    global id_count
    temp = id_count
    id_count += 1
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
