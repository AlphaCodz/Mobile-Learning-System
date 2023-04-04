from rest_framework.permissions import BasePermission
from auths.models import Primary

class IsStaff(BasePermission):
    message = "For YCT Staffs Only"
    def has_permission(self, request, view):
        staff = Primary.objects.filter(is_lecturer=True).exists()
        return staff
    