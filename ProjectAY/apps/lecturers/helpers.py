from auths.models import Primary

def Jsonify_staff(staff:Primary):
    return {
        "first name":staff.first_name,
        "last_name": staff.last_name,
        "email": staff.email,
        "staff id": staff.staff_id,
        "staff department": staff.department
    }