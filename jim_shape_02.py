from pprint import pprint


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations of the received arguments
        assert price > 0
        assert quantity >= 0

        # Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        print(f'{self.name} instance was created!')

        # Actions to execute
        Item.all.append(self)

    def calculate_total(self):
        return self.price * self.quantity

    def apply_disc(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self) -> str:
        price = "${:.2f}".format(self.price)
        return f'Name: {self.name}, Price: {price}, Qt: {self.quantity}'


item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 300, 6)
item3 = Item('Fernet', 5, 75)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
item6 = Item("Cable", 10, 5)


print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print('*' * 100)
print(item1.calculate_total())
item1.apply_disc()
print(item1.calculate_total())

print('*' * 100)
item2.pay_rate = 0.7  # Not default pay_rate
print(item2.calculate_total())
item2.apply_disc()
print(item2.calculate_total())

print('*' * 100)

pprint(Item.all)
print('*' * 100)
# ----------------------------------------------------------------------------------------------------
