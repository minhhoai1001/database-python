import warnings
from database import *
from sqlalchemy import desc, and_, or_, not_

warnings.filterwarnings("ignore")

cookie = session.query(Cookie).all()
# print(cookie)
print("Control columns: ", session.query(Cookie.cookie_name, Cookie.quantity).first())

print("\n ---------- ORDER ----------")
print("Order by cookie quatity")
for cookie in session.query(Cookie).order_by(Cookie.quantity):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

print("Order by quatity descending")
for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

print("Limit number query")
query = session.query(Cookie).order_by(Cookie.quantity)[:2]
print([result.cookie_name for result in query])

print("\n ---------- FILTERING ----------")
record = session.query(Cookie).filter(Cookie.cookie_name == 'dark chocolate chip').first()
# print(record)

print("Finding names with “chocolate” in them")
query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
for record in query:
    print(record.cookie_name)

print("Filter with condition")
query = session.query(Cookie).filter(Cookie.quantity> 5, Cookie.unit_cost< 0.78)
for result in query:
    print("with compare: ", result.cookie_name)

query = session.query(Cookie).filter(or_(Cookie.quantity> 5, Cookie.unit_cost< 0.78))
for result in query:
    print("with or condition: ", result.cookie_name)
