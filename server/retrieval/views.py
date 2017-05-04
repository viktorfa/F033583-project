from rest_framework.decorators import api_view
from rest_framework.response import Response

from retrieval.util import parse_index_fields, parse_filters, parse_ranking
from server.ir_project_server.wsgi import retriever


@api_view(['GET'])
def get_query(request, query):
    index_fields = parse_index_fields(request.GET.get('index'))
    filters = parse_filters(request.GET.get('filters'))
    ranker = parse_ranking(request.GET.get('ranking'))
    executed_query = retriever.retrieve(query, filters=filters, index=index_fields, ranker=ranker)
    data = dict(
        results=executed_query.get_sorted_results_with_analytics(),
        meta=executed_query.get_meta_information()
    )
    return Response(data)


@api_view(['POST'])
def click_result(request, query_id):
    return Response()
