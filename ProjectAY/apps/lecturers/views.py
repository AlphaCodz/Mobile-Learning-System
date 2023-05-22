from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from rest_framework.response import Response
from .helpers import Jsonify_staff
from rest_framework.decorators import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from .permissions import IsStaff
from students.models import Topic, Course
from students.helpers import jsonify_courses

# Create your views here.
class Profile(APIView):
    permission_classes = [IsStaff, ]
    def get(self, request, format=None):
        email = request.user.email
        try:
            staff = Primary.objects.get(email=email)
            if staff:
                staff_data = {
                    "code":200,
                    "message": "Successful",
                    "first name": staff.first_name,
                    "last_name": staff.last_name,
                    "staff_id": staff.staff_id,
                    "department": staff.department
                }
                return Response(staff_data, 200)
        except Exception as e:
            return {
                "code":400,
                "message": "User Not Found",
                "error": str(e)
            }
            
class CreateTopic(BaseView):
    required_post_fields=["name", "files", "notes"]
    def post(self, request, format=None):
        try:
            topic = Topic.objects.filter(name=request.data["name"]).exists()
            if topic:
                res = {
                    "code":400,
                    "message": "Topic already Exists"
                }
                return Response(res, 400)
            # call fields
            
            # create fields
            topic = Topic()
            topic.name = request.data["name"]
            topic.files = request.data["files"]
            topic.notes = request.data["notes"]
            topic.save()
            res = {
                "code": 201,
                "message": "Topic created successfully",
                "topic_data": {
                    "name": topic.name,
                    "file": topic.get_file_url() if topic.get_file_url() else None,
                    "note": topic.notes
                }
            }
            return Response(res, 201)
        except Exception as e:
            res = {
                "code": 400,
                "message": "Unsuccessful Please Try again",
                "error": str(e)
            }
            return Response(res, 400)
        
    

class AddCourse(BaseView):
    required_post_fields = ["title", "code", "description"]
    def post(self, request, format=None):
        super().post(request, format)
        course = Course()
        course.title = request.data["title"]
        course.code = request.data["code"]
        course.description = request.data["description"]
        course.save()
        resp = {
            "code":201,
            "message": "Course Added Successfully",
            "data": jsonify_courses(course) 
        }
        return Response(resp, 201)

class CreateLesson(APIView):
    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            resp = {
                "code": 404,
                "message": "Course Not Found"
            }
            return Response(resp, 404)
        
        lesson = Topic.objects.create(
            name=request.data["name"],
            files = request.data["files"],
            notes= request.data["notes"],
            course=course
        )
        lesson.save()
        resp = {
            "code": 201,
            "message": "Lesson Created Successfully",
            "lesson_data": {
                "name": lesson.name,
                "files": lesson.get_file_url(),
                "notes": lesson.notes,
                "course": lesson.course.title
            }
        }
        return Response(resp, 201)

class GetLessons(APIView):
    def get(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            resp = {
                "code": 404,
                "message": "Course Not Found"
            }
            return Response(resp, 404)
        lessons = course.lessons.all()
        data = [{"name":lesson.name, "files": lesson.get_file_url(), "notes":lesson.notes} for lesson in lessons]
        resp = {
            "code": 200,
            "message": "Successful",
            "data": data
        }
        return Response(resp, 200)
    
class UpdateLesson(APIView):
    def put(self, request, lesson_id):
        try:
            lesson = Topic.objects.get(id=lesson_id)
        except Topic.DoesNotExist:
            resp = {
                "code": 404,
                "message": "Lesson Not Found"
            }
            return Response(resp, 404)
        lesson.name = request.data.get("name", lesson.name)
        lesson.files = request.data.get("files", lesson.files)
        lesson.notes = request.data.get("notes", lesson.notes)
        lesson.save()
        resp = {
            "code": 200,
            "message": "Lesson Updated Successfully",
            "lesson_data": {
                "name": lesson.name,
                "files": lesson.get_file_url(),
                "notes": lesson.notes,
                # "course": lesson.course.title
            }
        }
        return Response(resp, 200)
        
        
    
class CreateTopic(BaseView):
    def post(self, request, course_id):
        course_id = Course.objects.get(id=course_id)
        
        
        


    
    
"""
ALGORITHM
1. CREATE COURSE
2. CREATE TOPIC
3. ADD TOPIC TO COURSE BY ID

"""
    