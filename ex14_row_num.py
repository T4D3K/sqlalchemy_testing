import datetime
import random

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, joinedload

from helpers import random_name, random_surname, random_date
from models import Account, User, Invoice, Product, InvoiceItem, ProductStock

engine = sa.engine.create_engine('sqlite:///litedb', echo=False)
session = sessionmaker(bind=engine)()
u1 = session.query(
    func.count(User.id).label('total')
)
u2 = session.query(
    func.count(Account.id)
)
u3 = session.query(
    func.count(Product.id)
)
u4 = session.query(
    func.count(ProductStock.id)
)
u5 = session.query(
    func.count(InvoiceItem.id)
)
u6 = session.query(
    func.count(Invoice.id)
)
u7 = u1.union_all(u2, u3, u4, u5, u6).subquery()
u = session.query(
     func.sum(u7.c.total)
).select_from(u7).scalar()
print(u)
