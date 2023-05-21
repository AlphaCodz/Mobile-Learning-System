from django.urls import path
from .views import Profile, AddCourse, CreateLesson

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("add/course", AddCourse.as_view(), name="add-course"),
    path("create/lesson/<int:course_id>", CreateLesson.as_view(), name="create-lesson")

]
