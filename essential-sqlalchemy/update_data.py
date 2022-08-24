from database import *
import warnings

warnings.filterwarnings("ignore")

print("Update via object -----")
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "dark chocolate chip").first()
cc_cookie.quantity += 100
session.commit()
print("Update quantiy of dark chocolate chip: ", cc_cookie.quantity)

print("Update data in place -----")
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "dark chocolate chip")
query.update({Cookie.quantity: Cookie.quantity - 20})

cc_cookie = query.first()
print("Update quantiy of dark chocolate chip: ", cc_cookie.quantity)