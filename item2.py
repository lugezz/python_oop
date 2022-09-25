import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations of the received arguments
        assert price > 0
        assert quantity >= 0

        # Assign to self object
        self.__name = name
        self.quantity = quantity
        self.__price = price

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @property
    # Property Decorator = Read-Only Attribute
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        if len(value) > 10:
            print(f"The name is too long!, I'll just take {value[:10]}")
            self.__name = value[:10]
        else:
            self.__name = value

    def calculate_total(self):
        return self.__price * self.quantity

    def apply_disc(self):
        self.__price = self.__price * Item.pay_rate

    def increment_price(self, increment_value):
        self.__price = self.__price * (1 + increment_value / 100)

    def __connect(self, smtp_test=''):
        pass

    def __prepare_body(self):
        pass

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

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
