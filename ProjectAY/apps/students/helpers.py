from .models import Course

def jsonify_courses(course:Course):
    return {
        "id": course.id,
        "course title": course.title,
        "course code": course.code,
        "course description": course.description
    }
    