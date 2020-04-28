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
    session.add(invoice)
    session.flush()
    products = []
    items = []
    for i in range(10000):
        product = {
            'name': random.choice(string.ascii_uppercase) + str(random.randint(1, 10000))
        }
        products.append(product)
        if not i % 999:
            session.execute(Product.__table__.insert(products))
            products = []
    session.execute(Product.__table__.insert(products))
    products = session.query(Product.id).all()
    for i,row in enumerate(products):
        invoice_item = {
            'invoice_id': invoice.id,
            'product_id': row.id,
            'quantity': 1,
            'price': 1
        }
        items.append(invoice_item)
        if not i % 249:
            session.execute(InvoiceItem.__table__.insert(items))
            items = []
    session.execute(InvoiceItem.__table__.insert(items))
    items = session.query(InvoiceItem)
    session.commit()
    # session.rollback()
