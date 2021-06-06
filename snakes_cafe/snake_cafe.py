print(" Welcome to the Snakes Cafe!")
print(" Please see our menu below.!")
print("To quit at any time, type 'quit'")

menu= """

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(" What would you like to order?")


order_menu={
    'Wings' :0,
    'cookies' :0,
    'Spring Rolls' :0,
    'Salmon' :0,
    'Steak' :0,
    'Meat Tornado' :0,
    'A Literal Garden' :0,
    'Ice Cream' :0,
    'Cake' :0,
    'Pie' :0,
    'Coffee' :0,
    'Tea' :0,
    'Unicorn Tears' :0
}

def order():
    print("your order")
    for x in order_menu:
        if order_menu[x] >0:
            print(f"** {order_menu[x]} orders of {x} have been added to your meal **")

def recieve_order():
    x=''
    print(menu)
    while x != 'quit':
        x=input('>')
        if x.capitalize() in order_menu:
           order_menu[x.capitalize()]+=1
           print(f"** {order_menu[x.capitalize()]} order of {x.capitalize()} have been added to your meal **")
        else:
           print(f"sorry {x} is not existing in the menu")
           


order()
        

recieve_order()






 