import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    date_of_birth = sa.Column(sa.Date)
    account = relationship('Account', uselist=False, back_populates='user')


class Account(Base):
    __tablename__ = 'account'

    id = sa.Column(sa.Integer, primary_key=True)
    login = sa.Column(sa.String)
    password = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    user = relationship('User', back_populates='account')
    invoices = relationship('Invoice', back_populates='account')


class Product(Base):
    __tablename__ = 'product'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    price = sa.Column(sa.Integer)
    stocks = relationship('ProductStock', back_populates='product')
    invoice_items = relationship('InvoiceItem', back_populates='product')


class ProductStock(Base):
    __tablename__ = 'product_stock'

    id = sa.Column(sa.Integer, primary_key=True)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('product.id'))
    purchase_price = sa.Column(sa.Integer)
    quantity = sa.Column(sa.Integer)
    product = relationship('Product', back_populates='stocks')


class Invoice(Base):
    __tablename__ = 'invoice'

    id = sa.Column(sa.Integer, primary_key=True)
    account_id = sa.Column(sa.Integer, sa.ForeignKey('account.id'))
    invoice_date = sa.Column(sa.Date)
    invoice_number = sa.Column(sa.String)
    invoice_amount = sa.Column(sa.Integer)
    account = relationship('Account', back_populates='invoices')
    invoice_items = relationship('InvoiceItem', back_populates='invoice')


class InvoiceItem(Base):
    __tablename__ = 'invoice_item'

    id = sa.Column(sa.Integer, primary_key=True)
    invoice_id = sa.Column(sa.Integer, sa.ForeignKey('invoice.id'))
    product_id = sa.Column(sa.Integer, sa.ForeignKey('product.id'))
    name = sa.Column(sa.String)
    price = sa.Column(sa.Integer)
    quantity = sa.Column(sa.Integer)
    discount = sa.Column(sa.Integer)
    invoice = relationship('Invoice', back_populates='invoice_items')
    product = relationship('Product', back_populates='invoice_items')
