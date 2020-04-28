import random
import sqlite3
import string

import sqlalchemy as sa

from helpers import Timer

connection = sqlite3.connect('litedb')
cursor = connection.cursor()
cursor.execute('DELETE FROM invoice')
cursor.execute('DELETE FROM invoice_item')
cursor.execute('DELETE FROM product')
cursor.execute('DELETE FROM product_stock')
connection.commit()
cursor.execute("SELECT id FROM account LIMIT 1")
account_id = cursor.fetchone()[0]

with Timer('raw'):
    cursor.execute('BEGIN')
    invoice_insert = f"INSERT INTO invoice (account_id, invoice_number) VALUES ({account_id}, 'test')"
    cursor.execute(invoice_insert)
    cursor.execute("SELECT last_insert_rowid()")

    invoice_id = cursor.fetchone()[0]
    products = []
    prd_insert = "INSERT INTO product (name) VALUES"
    for _ in range(10000):
        products.append(
            f"('{random.choice(string.ascii_uppercase) + str(random.randint(1, 10000))}')"
        )
    cursor.execute(prd_insert + ','.join(products))
    cursor.execute("SELECT id FROM product")
    prd_ids = cursor.fetchall()
    items = []
    item_insert = "INSERT INTO invoice_item (invoice_id, product_id, quantity, price) VALUES"
    for row in prd_ids:
        prd_id = row[0]
        items.append(
            f"({invoice_id}, {prd_id}, 1, 2)"
        )
    cursor.execute(item_insert + ','.join(items))
    cursor.execute('COMMIT')
    # cursor.execute('ROLLBACK')
