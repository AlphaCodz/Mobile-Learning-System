from django.shortcuts import render
from auths.models import Primary
from helpers.views import BaseView
from rest_framework.response import Response
from .helpers import Jsonify_staff
from rest_framework.decorators import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated
from .permissions import IsStaff

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
                "message": "User Not Logged in",
                "error": str(e)
            }
            
        
        
        
            
            
    