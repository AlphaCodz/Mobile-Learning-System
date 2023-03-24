from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from .permissions import IsStudent
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.helpers import jsonify_userdata

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
            
        