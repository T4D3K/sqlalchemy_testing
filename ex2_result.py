import sqlite3
import sqlalchemy as sa


engine = sa.engine.create_engine('sqlite:///litedb')
result_proxy = engine.execute('SELECT 1 as test')
r1 = result_proxy.fetchone()

print(r1)
print(r1.test)
print(type(r1))

connection = sqlite3.connect('litedb')
cursor = connection.cursor()
cursor.execute('SELECT 1 as test')
r2 = cursor.fetchone()

print('-'*20)
print(r2)
print(r2[0])
print(type(r2))
try:
    print(r2.test)
except AttributeError:
    print('Ups!!!')
