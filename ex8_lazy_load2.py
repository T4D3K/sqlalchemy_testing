import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User, Invoice, Product, InvoiceItem

engine = sa.engine.create_engine('sqlite:///litedb', echo=True)
session = sessionmaker(bind=engine)()

invoice = session.query(Invoice).first()

print(invoice.invoice_number, invoice.account.login, invoice.account.user.name, invoice.account.user.surname)
for item in invoice.invoice_items:
    print(item.name, item.quantity, item.product.name)
    for stock in item.product.stocks:
        print(stock.quantity, stock.purchase_price)