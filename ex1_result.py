import sqlalchemy as sa


engine = sa.engine.create_engine('sqlite:///litedb')
result_proxy = engine.execute('SELECT 1 as test')
r1 = result_proxy.fetchone()

print(r1)
print(r1.test)
print(type(r1))

