import csv


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
        with open('items2.csv', 'r') as f:
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
        return f'Class {self.__class__.__name__}, Name: {self.name}, Price: {price}, Qt: {self.quantity}'
