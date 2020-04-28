import datetime
import random
import string

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import Timer
from models import Account, Invoice, Product, InvoiceItem, ProductStock

engine = sa.engine.create_engine('sqlite:///litedb', echo=False)
session = sessionmaker(bind=engine)()

session.query(Invoice).delete()
session.query(InvoiceItem).delete()
session.query(Product).delete()
session.query(ProductStock).delete()
session.commit()

account = session.query(Account).first()
with Timer('Insert big invoice'):
    invoice = Invoice(
        account=account,
        invoice_number='test'
    )

    for _ in range(10000):
        product = Product(
            name=random.choice(string.ascii_uppercase) + str(random.randint(1, 10000))
        )

        invoice_item = InvoiceItem(
            invoice=invoice,
            product=product,
            quantity=1,
            price=1
        )

    session.add(invoice)
    session.commit()