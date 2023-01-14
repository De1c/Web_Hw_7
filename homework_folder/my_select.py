from sqlalchemy import select, func, desc

from database.db import session
from database.models import Teacher, Group, Student, Subject, Grade

    
def select_1():
    q = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc("avg_grade")).limit(5).all()
    print(q)
    
def select_2():
    q = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"), Subject.subject_name)\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id == 5).group_by(Subject.id, Student.id).order_by(desc("avg_grade")).limit(5).all()
    print(q)

def select_3():
    q = session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label("avg_grade"), Subject.subject_name)\
        .select_from(Grade).join(Student).join(Group).join(Subject).group_by(Group.id, Subject.id).order_by(Group.id).all()
    print(q)
    
def select_4():
    q = session.query(func.round(func.avg(Grade.grade), 2).label("avg_grade")).select_from(Grade).all()
    print(q)
    
def select_5():
    q = session.query(Subject.subject_name, Teacher.name).select_from(Teacher).join(Subject).group_by(Subject.id, Teacher.name).all()
    print(q)
    
def select_6():
    q = session.query(Student.name, Group.group_name).select_from(Group).join(Student).group_by(Student.name, Group.group_name, Group.id).order_by(Group.id).all()
    print(q)
    
def select_7():
    q = session.query(Group.group_name, Grade.grade, Subject.subject_name)\
        .select_from(Grade).join(Student).join(Group).join(Subject)\
        .filter(Subject.id == 4, Group.id == 1).group_by(Group.group_name, Subject.id, Grade.grade, Student.id).order_by(Grade.grade).all()
    print(q)
    
def select_8():
    q = session.query(Teacher.name, func.round(func.avg(Grade.grade), 2).label("avg_grade"), Subject.subject_name)\
        .select_from(Grade).join(Subject).join(Teacher).group_by(Teacher.id, Subject.id).order_by(Teacher.id).all()
    print(q)
    
def select_9():
    q = session.query(Student.name, Subject.subject_name).select_from(Grade).join(Subject).join(Student).filter(Student.id == 1).group_by(Student.id, Subject.id).all()
    print(q)
    
def select_10():
    q = session.query(Student.name, Subject.subject_name, Teacher.name).select_from(Grade).join(Subject).join(Student).join(Teacher)\
        .filter(Student.id == 1, Teacher.id == 1).group_by(Student.id, Teacher.id, Subject.id).all()
    print(q)

def add_select_1():
    q = session.query(Student.name, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label("avg_grade"), Teacher.name)\
        .select_from(Grade).join(Student).join(Subject).join(Teacher).filter(Student.id == 1, Teacher.id == 1).group_by(Student.id, Teacher.id, Subject.id).all()
    print(q)

def add_select_2():
    q = session.query(Grade.grade, func.max(Grade.grade_date), Student.name, Subject.subject_name, Group.group_name)\
        .select_from(Grade).join(Student).join(Subject).join(Group).filter(Group.id == 1, Subject.id == 1)\
            .group_by(Student.id,Subject.id, Grade.id, Group.id).order_by(Grade.grade_date).all()
    print(q)
    
if __name__ == '__main__':
    add_select_2()