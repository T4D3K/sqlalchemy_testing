import datetime
import random
import string

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from helpers import Timer, random_name, random_surname, random_date
from models import Account, Invoice, Product, InvoiceItem, ProductStock, User

engine = sa.engine.create_engine('sqlite:///litedb', echo=False)
session = sessionmaker(bind=engine)()

session.query(Invoice).delete()
session.query(InvoiceItem).delete()
session.query(Product).delete()
session.query(ProductStock).delete()
session.query(Account).delete()
session.query(User).delete()
session.commit()

account = session.query(Account).first()
with Timer('Insert big invoice'):
    for _ in range(1000):
        user = User(
            name=random_name(),
            surname=random_surname(),
            date_of_birth=random_date()
        )
        account = Account(
            user=user,
        )
        session.add(user)
        product = Product(
            name="".join(random.choices(string.ascii_uppercase, k=5)),
            price=random.randint(1,9)
        )
        stock = ProductStock(
            product=product,
            purchase_price=random.randint(1, 9)
        )
        session.add(product)
    session.commit()

    accounts = session.query(Account).all()
    products = session.query(Product).all()
    items = []
    for account in accounts:
        for _ in range(random.randint(1,5)):
            invoice = Invoice(
                account=account,
                invoice_number="".join(random.choices(string.ascii_uppercase, k=5)) + str(random.randint(0,9))
            )
            session.add(invoice)
            session.flush()
            for row in random.choices(products, k=random.randint(1,9)):
                invoice_item = InvoiceItem(
                    invoice_id=invoice.id,
                    product_id=row.id,
                    quantity=1,
                    name="Order: " + row.name,
                    price=row.price * 2
                )
                items.append(invoice_item)

    session.bulk_save_objects(items)
    session.commit()
    # session.rollback()
