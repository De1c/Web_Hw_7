from sqlalchemy.orm import joinedload

from database.db import session
from database.models import Student, Teacher

def get_students():
    students = session.query(Student).options(joinedload("teachers")).all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {teacher.id} name: {teacher.name}' for teacher in s.teachers]}")
    

def get_teachers():
    teachers = session.query(Teacher).options(joinedload("students")).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {student.id} name: {student.name}' for student in t.students]}")


if __name__ == "__main__":
    get_teachers()