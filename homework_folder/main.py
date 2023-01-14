from database.db import session
from database.models import Teacher, Student, Group, Grade, Subject

import argparse

parser = argparse.ArgumentParser(description="CRUD for postgres db")

parser.add_argument("-a", "--action", metavar="-a", type=str)
parser.add_argument("-m", "--model", metavar="-m", type=str)
parser.add_argument("--id", metavar="-id", type=int, default=None)
parser.add_argument("-n", "--name", metavar="-n", type=str)


my_dict = {
        "Teacher": Teacher,
        "Student": Student,
        "Group": Group,
        "Grade": Grade,
        "Subject": Subject,
}


def create(model :str, name: str, id: int = None) -> None:
    model = my_dict[model.capitalize()]
    data = model(name=name)
    session.add(data)
    session.commit()


def delete(model :str, name: str, id: int) -> None:
    model = my_dict[model.capitalize()]
    data = session.query(model).filter(model.id == id, model.name == name).first()
    session.delete(data)
    session.commit()


def update(model: str, name: str, id: int) -> None:
    model = my_dict[model.capitalize()]
    data = session.query(model).filter(model.id == id).first()
    print(data)
    data.name = name
    session.add(data)
    session.commit()


def get_list(model: str, name: str= None, id: int = None) -> None:
    model = my_dict[model.capitalize()]
    data = session.query(model.name).select_from(model).group_by(model.id).all()
    print(data)


def main(args):
    name = args.name
    model = args.model
    my_id = args.id
    crud_dict = {
        "create": create,
        "delete": delete,
        "update": update,
        "list": get_list
    }
    crud_dict[args.action](args.model, args.name, args.id)

if __name__ == "__main__":
    args = args = parser.parse_args()
    main(args)