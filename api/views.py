from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from .serializers import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .utils import *

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
        {
            'Endpoint': 'test',
            'method': ['GET', 'POST'],
            'title': None,
            'body': None,
            'description': 'Test Endpoint'
        },
        {
            'Endpoint': 'section',
            'method': ['GET', 'POST'],
            'title': None,
            'body': None,
            'description': 'Each section includes a topic'
        },
        {
            'Endpoint': 'section/id/topic',
            'method': ['GET', 'POST'],
            'title': None,
            'body': None,
            'description': 'Each topic includes a subtopic'
        },
        {
            'Endpoint': 'section/id/topic/id',
            'method': ['GET', 'POST'],
            'title': None,
            'body': None,
            'description': 'Subtopic for a particular topic'
        },
    ]

    return Response(routes)

# Content
# GET Content
@api_view(['GET', 'POST'])
def get_sections(request):
    if request.method == 'GET':
        return get_sections_list(request)
    
    if request.method == 'POST':
        return create_section(request)

@api_view(['GET', 'DELETE'])
def get_section(request, pk):
    if request.method == 'GET':
        return get_section_detail(pk)

    if request.method == 'DELETE':
        return delete_section(request, pk)


@api_view(['GET', 'POST'])
def get_topics(request, section_id=None):
    if request.method == 'GET':
        return get_topics_list(request, section_id)

@api_view(['GET', 'POST'])
def get_subtopics(request, section_id=None, topic_id=None):
    if request.method == 'GET':
        return get_subtopics_list(request, section_id, topic_id)

# Auth
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def test_endpoint(request):
    if request.method == 'GET':
        data = f"Hey {request.user}, you are seeing a GET response"

        return Response( 
            {
                'response':data
            }, 
            status=status.HTTP_200_OK
        )
    
    elif request.method == 'POST':
        text = request.POST.get('text')
        data = f"Hey {request.user}, this is POST data and your text is {text}"
        return Response( {'response':data}, status=status.HTTP_200_OK)
    return Response( {}, status=status.HTTP_400_BAD_REQUEST)