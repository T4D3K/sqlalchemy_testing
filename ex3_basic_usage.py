import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

account = Account(
    login='test',
    password='9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
)

user = User(
    name=random_name(),
    surname=random_surname(),
    date_of_birth=random_date()
)

account.user = user
session.add(account)
session.commit()