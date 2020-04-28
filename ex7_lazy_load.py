import datetime
import random

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import random_name, random_surname, random_date
from models import Account, User, Invoice, Product, InvoiceItem, ProductStock

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()


def add_invoice():
    account = session.query(Account).first()
    product = Product(
        name='Produkt testowy'
    )
    for _ in range(3):
        product.stocks.append(
            ProductStock(
                quantity=random.randint(1,10),
                purchase_price=1
            )
        )

    invoice = Invoice(
        account=account,
        invoice_amount=2,
        invoice_number='123',
        invoice_date=datetime.datetime.today()
    )

    for _ in range(5):
        invoice_item = InvoiceItem(
            product=product,
            name='Zakup: ' + product.name,
            quantity=1,
            price=2,
            discount=0
        )
        invoice.invoice_items.append(invoice_item)

    session.add(invoice)
    session.commit()


add_invoice()

invoice = session.query(Invoice).first()

print(invoice.invoice_number, invoice.account.login, invoice.account.user.name, invoice.account.user.surname)
for item in invoice.invoice_items:
    print(item.name, item.quantity, item.product.name)
    for stock in item.product.stocks:
        print(stock.quantity, stock.purchase_price)