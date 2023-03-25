from .models import Course

def jsonify_courses(course:Course):
    return {
        "course title": course.title,
        "course code": course.code,
        "course description": course.description
    }
    