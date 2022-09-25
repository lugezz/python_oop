class Item:

    def calculate_total(self):
        return self.price * self.quantity


item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

item2 = Item()
item2.name = 'Laptop'
item2.price = 250
item2.quantity = 3

print(item1.calculate_total())
print(item2.calculate_total())

print('*' * 100)
# ----------------------------------------------------------------------------------------------------


class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations of the received arguments
        assert price > 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        print(f'{self.name} instance was created!')

    def calculate_total(self):
        return self.price * self.quantity


item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 300)
item3 = Item('Fernet', 5, 75)

print(item1.calculate_total())
print(item2.calculate_total())
print(item3.calculate_total())

print('*' * 100)
# ----------------------------------------------------------------------------------------------------
