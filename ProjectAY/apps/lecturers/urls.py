from django.urls import path
from .views import Profile, CreateTopic, AddCourse

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("add/course", AddCourse.as_view(), name="add-course"),
    path("create/topic", CreateTopic.as_view(), name = "create-course"),
]
