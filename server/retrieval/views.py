from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from retrieval import search_log
from retrieval.util import parse_index_fields, parse_filters, parse_ranking
from server.ir_project_server.wsgi import retriever


@api_view(['GET'])
def get_query(request, query):
    index_fields = parse_index_fields(request.GET.get('index'))
    filters = parse_filters(request.GET.get('filters'))
    ranker = parse_ranking(request.GET.get('ranking'))
    executed_query = retriever.retrieve(query, filters=filters, index=index_fields, ranker=ranker)
    data = dict(
        results=executed_query.get_sorted_results_with_analytics()[:10],
        meta=executed_query.get_meta_information()
    )
    return Response(data)


@api_view(['POST'])
def click_result(request):
    query_id = request.GET.get('qid', None)
    song_id = request.GET.get('sid', None)
    print(query_id, type(query_id))
    print(song_id, type(query_id))
    if query_id is None or song_id is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    search_log.register_click(int(query_id), int(song_id))
    return Response(status=status.HTTP_202_ACCEPTED)
