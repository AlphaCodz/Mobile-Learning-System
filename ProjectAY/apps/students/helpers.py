from .models import Course

def jsonify_courses(course:Course):
    return {
        "id": course.id,
        "course_title": course.title,
        "course_code": course.code,
        "course_description": course.description
    }
    