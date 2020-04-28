import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

user = session.query(User).first()
print(user)
print(user.id, user.name, user.surname)

print('-' * 20)

users = session.query(
    User.id,
    User.name,
    User.surname
).all()
print(users)
for user in users:
    print(type(user))
    print(user.id, user.name, user.surname)
