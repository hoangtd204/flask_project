
from Database.configdb import load_students

students = load_students()
def read_student():
    return [student.to_dict() for student in students]
