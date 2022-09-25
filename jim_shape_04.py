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


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones

    def __repr__(self) -> str:
        return f'{super().__repr__()}, Broken: {self.broken_phones}'


phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Phone("jscPhonev20", 750, 7, 2)

pprint(Item.all)
print(phone1.calculate_total())
print(phone2.calculate_total())
