from .models import *
from .serializers import *
from rest_framework.response import Response
import json

# Section
def get_sections_list(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)

def create_section(request):
    data = request.data
    section = Section.objects.create(
        title=data['title'],
        subtitle=data['subtitle'],
        cover=data['cover']
    )

    serializer = SectionSerializer(section, many=False)
    return Response(serializer.data)

def get_section_detail(pk):
    section = Section.objects.get(id=pk)
    serializer = SectionSerializer(section, many=False)
    return Response(serializer.data)

def delete_section(request, pk):
    section = Section.objects.get(id=pk)
    section.delete()
    return Response("Section was deleted")

def update_section_detail(request, pk):
    data = request.data
    section = Section.objects.get(id=pk)
    serializer = SectionSerializer(instance=section, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# Topic
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