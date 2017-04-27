from copy import deepcopy
from pprint import pprint

from common.io import load_inverted_index, load_song_objects, write_inverted_index
from indexer.weighing import MatrixMaker, tokenize


class IndexProvider:
    def __init__(self, scraper_output_file_name='example_output.json'):
        self.scraper_output_file_name = scraper_output_file_name
        self.indices = {}

    def create_inverted_index(self, fields=list(['title'])):
        """
        Creates an inverted index and writes it to a file based on some structured input from the scraper,
        indexed by the specified fields.
        :param input_file_name:
        :param fields:
        :return:
        """
        song_objects = load_song_objects(self.scraper_output_file_name)

        documents = []

        for song in song_objects:
            documents.append(' '.join([value if key in fields else ' ' for key, value in song.items()]))

        inverted_index = {}

        for document_id, document in enumerate(documents):
            tokens = tokenize(document)
            token_counts = [(token, tokens.count(token),) for token in set(tokens)]
            for token, count in token_counts:
                if token in inverted_index.keys():
                    inverted_index[token][document_id] = count
                    inverted_index[token]['df'] += 1
                else:
                    inverted_index_entry = {
                        document_id: count,
                        'df': 1
                    }
                    inverted_index[token] = inverted_index_entry

        meta_information = dict(
            num_documents=len(documents),
            num_terms=len(inverted_index),
        )

        print("Created inverted index for %d objects over fields: %s" % (len(song_objects), str(fields)))
        pprint(meta_information)

        new_index_object = Index(inverted_index, fields, meta_information)
        write_inverted_index(new_index_object)

        self.indices[str(fields)] = new_index_object

        return new_index_object

    def get_inverted_index(self, fields):
        if str(fields) in self.indices.keys():
            return self.indices[str(fields)]

        existing_inverted_index = load_inverted_index(fields)
        if existing_inverted_index:
            meta_information = existing_inverted_index.pop('meta_information')
            new_index_object = Index(existing_inverted_index, fields, meta_information)
            self.indices[str(fields)] = new_index_object
            return new_index_object
        else:
            return self.create_inverted_index(fields)


class Index:
    def __init__(self, inverted_index, fields, meta_information, matrix_maker=MatrixMaker()):
        self.inverted_index = inverted_index
        self.fields = fields
        self.meta_information = meta_information
        self.matrix_maker = matrix_maker
        self.matrix = self.matrix_maker.get_weighted_document_matrix(self)

    def get_inverted_index(self):
        return self.inverted_index

    def get_meta_information(self):
        return self.meta_information

    def get_matrix(self):
        return self.matrix

    def get_matrix_maker(self):
        return self.matrix_maker

    def get_query_matrix(self, query):
        return self.matrix_maker.get_weighted_query_matrix(query, self)

    def get_fields(self):
        return self.fields

    def get_inverted_index_for_file(self):
        result = deepcopy(self.inverted_index)
        result['meta_information'] = self.meta_information
        return result
