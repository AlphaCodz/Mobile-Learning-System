from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from rest_framework.response import Response
from .helpers import Jsonify_staff

# Create your views here.
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
            
    