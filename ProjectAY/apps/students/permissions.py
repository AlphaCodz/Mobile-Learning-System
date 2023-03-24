from rest_framework import permissions, status
from auths.models import Primary

class IsStudent(permissions.BasePermission):
    message= "Only Students Allowed"
    def has_permission(self, request, view):
        email= request.user.email
        student = Primary.objects.filter(email=email).exists()
        return student