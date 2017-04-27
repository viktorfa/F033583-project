from retrieval.ranker import Ranker, DateRanker
from typing import cast


def parse_index_fields(string):
    if not string:
        return 'default'
    else:
        return string.split(',')


def parse_filters(string):
    result = []
    if string is None:
        return result
    for filter_string in string.split(','):
        result.append(get_filter_function(*filter_string.split(':')))

    return result


def get_filter_function(field, operator, value):
    if operator == 'gte':
        return lambda x: x[field] >= type(x[field])(value)
    elif operator == 'lte':
        return lambda x: x[field] >= type(x[field])(value)
    elif operator == 'eq':
        return lambda x: x[field] == type(x[field])(value)
    elif operator == 'neq':
        return lambda x: x[field] != type(x[field])(value)
    else:
        raise Exception


def parse_ranking(string):
    if string == 'relevancy':
        return Ranker(relevancy=100, popularity=0)
    elif string == 'popularity':
        return Ranker(relevancy=0, popularity=100)
    elif string == 'date':
        return DateRanker()
    else:
        return Ranker()
