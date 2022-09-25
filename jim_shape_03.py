import csv
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity'])
            )

    @staticmethod
    def is_integer(value):
        return isinstance(value, int)

    def __repr__(self) -> str:
        price = "${:.2f}".format(self.price)
        return f'Name: {self.name}, Price: {price}, Qt: {self.quantity}'


Item.instantiate_from_csv()
pprint(Item.all)

print('*' * 100)
print(Item.is_integer(33.2))
print(Item.is_integer(33))
print(Item.is_integer(round(33.2)))

print('*' * 100)
# ----------------------------------------------------------------------------------------------------
