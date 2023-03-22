from django.shortcuts import render
from helpers.views import BaseView
from .models import Primary
from rest_framework.response import Response

# Create your views here.
class CreateUser(BaseView):
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
            
        
        
        