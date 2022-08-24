from database import *
import warnings

warnings.filterwarnings("ignore")

print("Insert sigle table -----")
dcc = Cookie(cookie_name='chocolate chip',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
            cookie_sku='C04',
            quantity=10,
            unit_cost=1.75)
mol = Cookie(cookie_name='fish',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
            cookie_sku='FS1',
            quantity=20,
            unit_cost=0.95)

# session.add(dcc)
# session.add(mol)
# session.commit()

cookiemon = User(username='cookiemon',
                email_address='mon@cookie.com',
                phone='111-111-1111',
                password='password')
cakeeater = User(username='cakeeater',
                email_address='cakeeater@cake.com',
                phone='222-222-2222',
                password='password')
pieperson = User(username='pieperson',
                email_address='person@pie.com',
                phone='333-333-3333',
                password='password')

# session.add(cookiemon)
# session.add(cakeeater)
# session.add(pieperson)
# session.commit()

print("Insert relationship table -----")
print("add user cookiemon")
o1 = Order()
o1.user = cakeeater
# session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name == "chocolate chip").first()
line1 = LineItem(cookie=cc, quantity=2, extended_cost=1.00)

fish = session.query(Cookie).filter(Cookie.cookie_name=="fish").first()
line2 = LineItem(quantity=12, extended_cost=3.00)
line2.cookie = fish
line2.order = o1

o1.line_items.append(line1)
o1.line_items.append(line2)
session.commit()