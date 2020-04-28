import datetime
import random
import string

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import Timer
from models import Account, Invoice, Product, InvoiceItem, ProductStock

engine = sa.engine.create_engine('sqlite:///litedb', echo=True)
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
    for _ in range(10000):
        product = Product(
            name=random.choice(string.ascii_uppercase) + str(random.randint(1, 10000))
        )
        products.append(product)
    # session.bulk_save_objects(products)  # we need to fix it
    session.bulk_save_objects(products, return_defaults=True)
    session.flush()
    for row in products:
        invoice_item = InvoiceItem(
            invoice_id=invoice.id,
            product_id=row.id,
            quantity=1,
            price=1
        )
        items.append(invoice_item)

    session.bulk_save_objects(items)
    items = session.query(InvoiceItem)
    session.commit()
