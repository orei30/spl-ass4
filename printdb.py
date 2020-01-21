import os
from persistence import *

products = repo.products.find_all()
for product in products:
    print(product.description)