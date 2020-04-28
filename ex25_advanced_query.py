import sqlite3
import sqlalchemy as sa

from helpers import Timer

connection = sqlite3.connect('litedb')
cursor = connection.cursor()
with Timer('query'):
    cursor.execute("""SELECT sum(invoice_item.price) AS total, user.name AS user_name, user.surname AS user_surname
    FROM user
           JOIN account ON user.id = account.user_id
           JOIN invoice ON account.id = invoice.account_id
           JOIN invoice_item ON invoice.id = invoice_item.invoice_id
    WHERE account.id IN (SELECT A.account_id
                         FROM (SELECT count(invoice.id) AS total, invoice.account_id AS account_id
                               FROM invoice
                               GROUP BY invoice.account_id) AS A
                         WHERE A.total = (SELECT max(B.total) AS max_1
                                               FROM (SELECT count(invoice.id) AS total
                                                     FROM invoice
                                                     GROUP BY invoice.account_id) AS B))
    GROUP BY user.name, user.surname
    ORDER BY sum(invoice_item.price) DESC""")
    r2 = cursor.fetchall()
print(r2)
for row in r2:
    print(row[1], row[2], "Total value", row[0])

