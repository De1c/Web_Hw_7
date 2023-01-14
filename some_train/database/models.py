from sqlalchemy import Column, Integer, String, Boolean, func, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())
    email =  Column(String(150), nullable=True)
    start_work = Column(Date, nullable=True)
    
    students = relationship("Student", secondary="teacher_to_students", back_populates="teachers", passive_deletes=True)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=True)
    email =  Column(String(150), nullable=True)
    
    teachers = relationship("Teacher", secondary="teacher_to_students", back_populates="students", passive_deletes=True)

# Таблица tags, где хранится набор тегов для списка дел.
class TeacherStudent(Base):
    __tablename__ = "teacher_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column("teacher_id", ForeignKey("teachers.id", ondelete="CASCADE"))
    student_id = Column("student_id", ForeignKey("students.id", ondelete="CASCADE"))