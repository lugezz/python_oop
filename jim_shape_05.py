from pprint import pprint

from phone import Phone


phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Phone("jscPhonev20", 750, 7, 2)

pprint(Phone.all)
print(phone1.calculate_total())
print(phone2.calculate_total())

print('*' * 100)

Phone.instantiate_from_csv()
pprint(Phone.all)
print('*' * 100)
