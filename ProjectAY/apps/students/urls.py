from django.urls import path
from .views import UserProfile, AllCourses

urlpatterns = [
    path("profile/<int:id>", UserProfile.as_view(), name="profile"),
    path("all/courses", AllCourses.as_view(),name="all-courses"),
    # path("search", SearchView.as_view(), name="search")
]