from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from .permissions import IsStudent
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.helpers import jsonify_userdata
from .models import Course, Lesson
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
