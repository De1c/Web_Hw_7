from faker import Faker

from database.db import session
from database.models import Teacher
    
fake = Faker("uk_UA")

def create_teachers():
    for _ in range(1, 6):
        teacher = Teacher(
            name=fake.name(),
            email=fake.ascii_free_email(),
            start_work=fake.date_between(start_date="-5y"),
        )
        session.add(teacher)
    session.commit()
    
if __name__ == "__main__":
    create_teachers()