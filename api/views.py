from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '',
            'method': 'GET',
            'title': None,
            'body': None,
            'description': 'Routes'
        },
    ]

    return Response(routes)