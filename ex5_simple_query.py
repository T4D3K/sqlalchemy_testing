import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

user = session.query(User).first()
print(user.id, user.name, user.surname)

print('-' * 20)
users = session.query(User).all()
print(users)
for user in users:
    print(user.id, user.name, user.surname)
