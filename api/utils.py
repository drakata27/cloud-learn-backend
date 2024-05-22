from .models import *
from .serializers import *
from rest_framework.response import Response
import json

def get_sections_list(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)

def get_topics_list(request, section_id):
    topics = Topic.objects.filter(section_id=section_id)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

def get_subtopics_list(request, section_id, topic_id):
    subtopics = Subtopic.objects.filter(
        topic_id=topic_id, 
        topic__section_id=section_id
    )
    serializer = SubtopicSerializer(subtopics, many=True)
    return Response(serializer.data)