from django.urls import path
from .views import UserProfile, AddCourse, AllCourses, AddTopic, SearchView

urlpatterns = [
    path("profile/<int:id>", UserProfile.as_view(), name="profile"),
    path("add/course", AddCourse.as_view(), name="add-course"),
    path("all/courses", AllCourses.as_view(),name="all-courses"),
    path("add/topic/<int:id>", AddTopic.as_view(), name = "create-course"),
    path("search", SearchView.as_view(), name="search")
]