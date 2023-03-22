from django.shortcuts import render
from helpers.views import BaseView
from .models import Primary
from rest_framework.response import Response
from .helpers import jsonify_userdata

# Create your views here.
class CreateStudentUser(BaseView):
    required_post_fields = ["first_name", "last_name", "email", "matric_number", "year", "department"]
    def post(self, request, format=None):
        res = super().post(request, format)
        if res:
            return res
        
        email = request.data["email"]
        user = Primary.objects.filter(email=email).first()
        if user:
            resp = {
                "code": 400,
                "message": "We regret to inform you that an account with the email address provided already exists in our system. Please try logging in with your email and password."
            }
            return Response(resp, 400)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.email = request.data["email"]
        user.matric_number = request.data["matric_number"]
        user.department = request.data["department"]
        user.year = request.data["year"]
        user.set_password(raw_password= request.data["password"])
        user.save()
        resp = {
            "code":201,
            "message":"Student Registered Successfully",
            "student-user": jsonify_userdata(user) 
        }
        return Response(resp, 201)
    
        
        
        
        
        
        