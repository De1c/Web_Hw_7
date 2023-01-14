from faker import Faker

from database.db import session
from database.models import Student
    
fake = Faker("uk_UA")

def create_students():
    for _ in range(1, 6):
        student = Student(
            name=fake.name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
        )
        session.add(student)
    session.commit()
    
if __name__ == "__main__":
    create_students()