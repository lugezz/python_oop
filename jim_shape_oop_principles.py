from item2 import Item

# 1) Encapsulation --------------------------------------------------------------------------------------

"""
Used when

* self.__name = name
* if len(value) > 10: validation

"""

item1 = Item('Notebook', 655, 4)
print(item1.price)

item1.increment_price(10)
print(item1.price)


# 2) Abstraction --------------------------------------------------------------------------------------
"""
Show just necessary info and hide the rest
"""

# I can't see private internal methods of send_email() (connect, prepare_body and send)
item1.send_email()

# 3) Inheritance --------------------------------------------------------------------------------------
"""
Used in Phone inheritance from Item
"""

# 4) Polymorphism --------------------------------------------------------------------------------------
name = "Artime"  # str
print(len(name))

some_list = ["some", "name"]  # list
print(len(some_list))
# That's polymorphism in action, a single function does now
# how to handle different kinds of objects as expected!


class Keyboard(Item):
    pay_rate = 0.7

    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )


keyb1 = Keyboard('Apple', 3000)
keyb1.apply_disc()
print(keyb1.price)
