from django.urls import path
from .views import Profile, AddCourse, CreateLesson, GetLessons, UpdateLesson

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("add/course", AddCourse.as_view(), name="add-course"),
    path("create/lesson/<int:course_id>", CreateLesson.as_view(), name="create-lesson"),
    path("lessons/<int:course_id>", GetLessons.as_view(), name="get-lessons"),
    path("edit/lesson/<int:lesson_id>", UpdateLesson.as_view(), name="update-lesson")

]
