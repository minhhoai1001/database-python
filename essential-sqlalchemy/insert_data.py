import database

dcc = database.Cookie(cookie_name='blue chocolate chip',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
            cookie_sku='BC03',
            quantity=10,
            unit_cost=0.75)
mol = database.Cookie(cookie_name='snack',
            cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
            cookie_sku='SNA1',
            quantity=8,
            unit_cost=0.80)

database.session.add(dcc)
database.session.add(mol)
database.session.commit()

# print(cc_cookie.cookie_id)