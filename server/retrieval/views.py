from rest_framework.decorators import api_view
from rest_framework.response import Response

from server.ir_project_server.wsgi import retriever


@api_view(['GET'])
def get_query(request, query):
    executed_query = retriever.retrieve(query)
    results = executed_query.get_sorted_results_with_analytics()
    return Response(results)
