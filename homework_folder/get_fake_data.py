import faker 
import sqlite3
from datetime import datetime
from random import choice, randint, randrange
from database.db import session
from database.models import Student, Teacher, Subject, Grade, Group

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 5
MAX_GRADES_FOR_STUDENT = 10

def generate_fake_data(number_students, number_teachers) -> tuple():
    fake_student_names = []
    fake_teacher_names = []
    fake_student_emails = []
    fake_teacher_emails = []

    fake = faker.Faker()
    
    for _ in range(number_students):
        fake_student_names.append(fake.name())
        fake_student_emails.append(fake.email())

    for _ in range(number_teachers):
        fake_teacher_names.append(fake.name())
        fake_teacher_emails.append(fake.email())

    subject_list = ["english","math","art","science","history"]    
    
    return fake_student_names, fake_student_emails, fake_teacher_names, fake_teacher_emails, subject_list

def data_to_db(student_names, student_emails, teacher_names, teacher_emails, subject_list):
    
    student_id = 0
    fake = faker.Faker()
    
    for student in student_names:
        student_id += 1
        if student_id <= 10:
            student = Student(name=student, email=student_emails.pop(randrange(len(student_emails))), group_id=1)
        elif student_id > 10 and student_id <= 20:
            student = Student(name=student, email=student_emails.pop(randrange(len(student_emails))), group_id=2)
        else:
            student = Student(name=student, email=student_emails.pop(randrange(len(student_emails))), group_id=3)
        session.add(student)
            
    for teacher in teacher_names:
        teacher = Teacher(name=teacher, email=teacher_emails.pop(randrange(len(teacher_emails))))
        session.add(teacher)
        
    for num in range(1, NUMBER_GROUPS+1):
        group = Group(group_name=f"{num}-{num}", number_of_students=int(NUMBER_STUDENTS/NUMBER_GROUPS))
        session.add(group)
    
    for num, subject in enumerate(subject_list):
        num += 1
        subject = Subject(subject_name=subject, teacher_id=num)
        session.add(subject)
    
    for student_id in range(1, NUMBER_STUDENTS+1):
        for subject_id in range(1, len(subject_list)+1):
            for grades_num in range(randint(1, MAX_GRADES_FOR_STUDENT)):
                grade = Grade(grade=randint(1, 5), grade_date=fake.date_between(start_date="-1y", end_date="today"), student_id=student_id, subject_id=subject_id)
                session.add(grade)

    session.commit()

if __name__ == '__main__':
    data_to_db(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS))