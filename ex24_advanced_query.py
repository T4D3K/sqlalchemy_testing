import datetime
import random
import string

import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from helpers import Timer, random_name, random_surname, random_date
from models import Account, Invoice, Product, InvoiceItem, ProductStock, User

engine = sa.engine.create_engine('sqlite:///litedb', echo=False)
session = sessionmaker(bind=engine)()
# sumaryczna cena per osoba dla tych z największą ilością faktur
with Timer('query'):
    count_invoices = session.query(
        func.count(Invoice.id).label('total'),
        Invoice.account_id
    ).group_by(Invoice.account_id).subquery()

    max_count = session.query(
        func.max(count_invoices.c.total)
    ).subquery()

    max_acc = session.query(
        count_invoices.c.account_id
    ).filter(count_invoices.c.total == max_count).subquery()

    result = session.query(
        func.sum(InvoiceItem.price).label('total'),
        User.name,
        User.surname,
    ).join(
        User.account,
        Account.invoices,
        Invoice.invoice_items
    ).filter(
        Account.id.in_(max_acc)
    ).group_by(User.name, User.surname).order_by(func.sum(InvoiceItem.price).desc()).all()

for row in result:
    print(row.name, row.surname, "Total value", row.total)