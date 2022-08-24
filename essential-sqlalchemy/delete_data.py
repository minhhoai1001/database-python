from database import *
import warnings

warnings.filterwarnings("ignore")

print("Delete via object -----")
query = session.query(Cookie).filter(Cookie.cookie_name == "blue chocolate chip")
dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()
dcc_cookie = query.first()
print("Delete blue chocolate: ", dcc_cookie)

print("Delete data in place -----")
query = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip")
query.delete()
mol_cookie = query.first()
print("Delete chocolate chip: ", mol_cookie)