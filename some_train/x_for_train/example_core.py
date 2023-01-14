from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

metadata = MetaData()
engine = create_engine("sqlite:///:memory:")

users = Table('users', metadata,
    Column("id", Integer, primary_key=True),
    Column("fullname", String),
)

addresses = Table('addresses', metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("email", String, nullable=False)
)

metadata.create_all(engine)

if __name__ == "__main__":
    with engine.connect() as conn:
        # ------ Дадати користувачів
        new_user = users.insert().values(fullname="Alexander Incognito")
        result_insert_user = conn.execute(new_user)
        # ------ Знайти користувачів
        user_select = select(users)
        print(user_select)
        result = conn.execute(user_select)
        for res in result:
            print(res)
        # ------ Додати адресу
        new_address = addresses.insert().values(email="alex@gmail.com", user_id=result_insert_user.lastrowid)
        result_insert_adress = conn.execute(new_address)
        # ------ Знайти адресу
        address_select = select(addresses)
        result = conn.execute(address_select)
        for address in result:
            print(address)
        # ------ JOIN
        address_select = select(addresses.c.email, users.c.fullname).join(users)
        result = conn.execute(address_select)
        for address in result:
            print(address)