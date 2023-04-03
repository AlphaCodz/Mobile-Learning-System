from .views import RegLecturer
from django.urls import path

urlpatterns = [
    path("reg/", RegLecturer.as_view(), name="reg-staff")
]
