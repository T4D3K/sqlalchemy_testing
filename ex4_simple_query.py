import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

for _ in range(4):
    user = User(
        name=random_name(),
        surname=random_surname(),
        date_of_birth=random_date()
    )
    account = Account(
        login='test',
        password='test',
        user=user
    )
    session.add(user)
session.commit()

user = session.query(User).first()
print(user.id, user.name, user.surname)
