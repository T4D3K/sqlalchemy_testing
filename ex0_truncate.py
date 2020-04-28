import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from models import Invoice, InvoiceItem, Product, ProductStock, Account, User

engine = sa.engine.create_engine('sqlite:///litedb')
session = sessionmaker(bind=engine)()

session.query(Invoice).delete()
session.query(InvoiceItem).delete()
session.query(Product).delete()
session.query(ProductStock).delete()
session.query(Account).delete()
session.query(User).delete()
session.commit()
