class SearchLog:
    def __init__(self):
        self.query_log = {}
        self.id_count = 0

    def register_click(self, query_id, song_id):
        pass

    def register_query(self, query):
        query_id = self._get_query_id()
        self.query_log[query_id] = query
        return query_id

    def _get_query_id(self):
        temp = self.id_count
        self.id_count += 1
        return temp
