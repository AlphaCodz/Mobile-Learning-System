from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from rest_framework.response import Response
from .helpers import Jsonify_staff
from rest_framework.decorators import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from .permissions import IsStaff
from students.models import Topic

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
    
    
    
    
"""
ALGORITHM
1. CREATE COURSE
2. CREATE TOPIC
3. ADD TOPIC TO COURSE BY ID

"""
    