from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from .permissions import IsStudent
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.helpers import jsonify_userdata
from .models import Course, Topic
from.helpers import jsonify_courses
from rest_framework import status
from django.db.models import Q

# Create your views here.

class UserProfile(APIView):
    # permission_classes = [IsStudent, ]
    def get(self, request, id):
        student = Primary.objects.filter(id=id).first()
        if not student:
            resp = {
                "code": 404,
                "message": "Student is not Found"
            }   
            return Response(resp, 404)
        resp = {
            "code":200,
            "message":"success",
            "student": jsonify_userdata(student)
        }     
        return Response(resp, 200)

class AddCourse(BaseView):
    required_post_fields = ["title", "code", "description"]
    def post(self, request, format=None):
        super().post(request, format)
        
        course = Course(title=request.data["title"])
        course.code = request.data["code"]
        course.description = request.data["description"]
        course.save()
        resp = {
            "code":201,
            "message": "Course Added Successfully",
            "data": jsonify_courses(course) 
        }
        return Response(resp, 201)

class AllCourses(APIView):
    def get(self, request):
        course = Course.objects.all()
        lis = []
        for courses in course:
            data = {
                "courses": jsonify_courses(courses)
            }
            lis.append(data)
            context = {"courses":lis}
        return Response(context, 200)

class AddTopic(APIView):
    def post(self, request, id):
        try:
            course = Course.objects.get(id=id)
        except Course.DoesNotExist:
            return Response({"error": "Course does not exist"}, status=status.HTTP_404_NOT_FOUND)

        topics_data = request.data.get("topics")
        if not isinstance(topics_data, list):
            return Response({"error": "Invalid topics data format. Expected a list of topics."}, status=status.HTTP_400_BAD_REQUEST)

        topics = []
        for topic_data in topics_data:
            name = topic_data.get("name")
            notes = topic_data.get("notes")
            note_file = topic_data.get("note_file")
            topic = Topic.objects.create(name=name, notes=notes, note_file=note_file, course=course)
            topics.append({
                "name": topic.name,
                "notes": topic.notes,
                "note_file_url": topic.get_file_url()
            })

        resp = {
            "code": 201,
            "message": "Topics created successfully",
            "course": {
                "title": course.title,
                "code": course.code,
                "description": course.description,
                "topics": topics
            }
        }
        return Response(resp, 201)
    

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if not query:
            return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)

        courses = Course.objects.filter(
            Q(title__icontains=query) | 
            Q(code__icontains=query) |
            Q(topics__name__icontains=query)
        ).distinct()

        results = [{
            "title": course.title,
            "code": course.code,
            "description": course.description,
            "topics": [{
                "name": topic.name,
                "notes": topic.notes,
                "note_file_url": topic.get_file_url()
            } for topic in course.topics.all()]
        } for course in courses]

        return Response({"results": results}, status=status.HTTP_200_OK)
    
