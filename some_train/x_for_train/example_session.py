from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///:memory:')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()

class Person(Base):
    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id')) # → For SQL tables
    person = relationship(Person) # → For SQLAlchemy users

Base.metadata.create_all(engine)
Base.metadata.bind = engine



if __name__ == "__main__":
    new_person = Person(name="Alexander Incognito")
    session.add(new_person) # After "add" DB do not recieve this data
    
    new_adress = Address(street_name="Stepana Giga", post_code="36800", person=new_person)
    session.add(new_adress)
    
    session.commit()        # It will only recieve it after "commit"
    print(new_person.id)
    # ----- Query -----
    person = session.query(Person).one()
    print(f"{vars(person)=}, {person.id=}, {person.name=}")
    # ----- JOIN -----
    addresses = session.query(Address).join(Address.person).all()
    for row in addresses:
        print(vars(row))
        print(row.person.name) # This shit we can implement thanks to "relationship" function in SQLAlchemy