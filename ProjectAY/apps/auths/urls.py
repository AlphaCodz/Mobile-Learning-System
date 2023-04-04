from django.urls import path
from .views import Login, CreateStudentUser, RegLecturer, LoginStaff

urlpatterns = [
    path("signup/student", CreateStudentUser.as_view(), name="create-student"),
    path("login/student", Login.as_view(), name="login-student"),
    path("login/staff", LoginStaff.as_view(), name="login-staff"),
    path("reg/", RegLecturer.as_view(), name="reg-staff")
]
