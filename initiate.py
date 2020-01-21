import os

if os.path.isfile('moncafe.db'):
    os.remove('moncafe.db')

from persistence import *

repo.create_tables()
# repo.init_tables()

with open('config.txt', 'r') as reader:
    for line in reader.readlines():
        words = line.split(',')
        if words[0] == 'C':
            repo.coffeeStands.insert(CoffeeStand(words[1].strip(), words[2].strip(), words[3].strip()))
        if words[0] == 'S':
            repo.suppliers.insert(Supplier(words[1].strip(), words[2].strip(), words[3].strip()))
        if words[0] == 'E':
            repo.employees.insert(Employee(words[1].strip(), words[2].strip(), words[3].strip(), words[4].strip()))
        if words[0] == 'P':
            repo.products.insert(Product(words[1].strip(), words[2].strip(), words[3].strip(), 0))