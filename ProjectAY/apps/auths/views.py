from django.shortcuts import render
from helpers.views import BaseView
from .models import Primary
from rest_framework.response import Response
from .helpers import jsonify_userdata
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from lecturers.helpers import Jsonify_staff

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
        student = Primary(first_name=request.data["first_name"])
        student.last_name = request.data["last_name"]
        student.email = request.data["email"]
        student.matric_number = request.data["matric_number"]
        student.department = request.data["department"]
        student.year = request.data["year"]
        student.set_password(raw_password= request.data["password"])
        student.save()
        resp = {
            "code":201,
            "message":"Student Registered Successfully",
            "student-user": jsonify_userdata(student) 
        }
        return Response(resp, 201)
    
    
class Login(BaseView):
    required_post_fields = ["matric_number", "password"]
    def post(self, request, format=None):
        res = super().post(request, format)
        if res:
            return res
        user = Primary.objects.filter(matric_number=request.data["matric_number"]).first()
        if not user:
            res = {
                "code":400,
                "message":"invalid credentials"
            }
            return Response(res, 400)
        if user.check_password(raw_password=request.data["password"]):
            token = RefreshToken.for_user(user)
            print(token)
            res = {
                "code":200,
                "message":"success",
                "student": jsonify_userdata(user),
                "token":str(token.access_token),
            }
            return Response(res, 200)
        else:
            res = {
                "code":400,
                "message":"invalid credentials"
            }
            return Response(res, 400)
        
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# STAFF VIEW
class RegLecturer(BaseView):
    required_post_fields = ["first_name", "last_name", "email", "staff_id", "department", "password"]
    def post(self, request, format=None):
        staff_id = request.data.get("staff_id")
        email= request.data.get("email")
        # Check if Staff id exists
        if Primary.objects.filter(staff_id=staff_id, email=email).exists():
            res = {
                "code":400,
                "message":"Staff has an account already!"
            }   
            return Response(res, 400)
        
        staff = Primary.objects.create(
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            email=request.data["email"],
            staff_id=request.data["staff_id"],
            department=request.data["department"],
        )
        staff.set_password(raw_password=request.data["password"])
        staff.save()
        res = {
            "code":201,
            "message":"Staff Account Created Successfully",
            "staff data": Jsonify_staff(staff)
        }
        return Response(res, status=201)
    
        
        
        