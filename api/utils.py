from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
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
    else:
        print("Serializer error", serializer.errors)
    return Response(serializer.data)

# Topic
def get_topics_list(request, section_id):
    topics = Topic.objects.filter(section_id=section_id)
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)

def create_topic(request, section_id):
    data = request.data

    try:
        section = Section.objects.get(id=section_id)
    except Section.DoesNotExist:
        return Response({"error": "Section not found."}, status=status.HTTP_404_NOT_FOUND)

    topic = Topic.objects.create(
        title=data['title'],
        subtitle=data['subtitle'],
        cover=data['cover'],
        section=section
    )

    serializer = TopicSerializer(topic, many=False)
    
    return Response(serializer.data)

def get_topic_detail(section_id, pk):
    section = Section.objects.get(id=section_id)
    topic = Topic.objects.get(id=pk, section=section)
    serializer = TopicSerializer(topic, many=False)
    return Response(serializer.data)

def delete_topic(section_id, pk):
    section = Section.objects.get(id=section_id)
    topic = Topic.objects.get(id=pk, section=section)
    topic.delete()
    return Response("Topic was deleted")

def update_topic_detail(request, section_id, pk):
    data = request.data
    section = Section.objects.get(id=section_id)
    topic = Topic.objects.get(id=pk, section=section)
    serializer = TopicSerializer(instance=topic, data=data)

    if serializer.is_valid():
        serializer.save()
    else:
        print("Serializer error", serializer.errors)
    return Response(serializer.data)

# Subtopics
def get_subtopics_list(request, section_id, topic_id):
    subtopics = Subtopic.objects.filter(
        topic_id=topic_id, 
        topic__section_id=section_id
    )
    serializer = SubtopicSerializer(subtopics, many=True)
    return Response(serializer.data)