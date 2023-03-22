from .models import Primary

def jsonify_userdata(user:Primary):
    return {
        "id":user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "matric_no": user.matric_number,
        "year": user.year,
        "department": user.department
    }
    