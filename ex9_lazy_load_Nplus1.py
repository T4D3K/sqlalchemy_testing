import datetime
import random

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User, Invoice, Product, InvoiceItem, ProductStock

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

accounts = session.query(Account).all()


def add_invoice():
    product = Product(
        name=f'Produkt testowy {random.randint(1, 1000)}'
    )
    for _ in range(3):
        product.stocks.append(
            ProductStock(
                quantity=random.randint(1,10),
                purchase_price=1
            )
        )
    invoice = Invoice(
        account=random.choice(accounts),
        invoice_amount=10,
        invoice_number=str(random.randint(1, 9) * 100 + random.randint(0, 9) * 10 + random.randint(0, 9)),
        invoice_date=datetime.datetime.today()
    )

    for _ in range(5):
        invoice_item = InvoiceItem(
            product=product,
            name=product.name,
            quantity=1,
            price=2,
            discount=0
        )
        invoice.invoice_items.append(invoice_item)

    session.add(invoice)
    session.commit()


for _ in range(4):
    add_invoice()

invoices = session.query(Invoice).all()

for invoice in invoices:
    print(invoice.invoice_number, invoice.account.login, invoice.account.user.name, invoice.account.user.surname)
    for item in invoice.invoice_items:
        print(item.name, item.quantity, item.product.name)
        for stock in item.product.stocks:
            print(stock.quantity, stock.purchase_price)
