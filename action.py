import os
import sys
from persistence import *

with open(sys.argv[1], 'r') as reader:
    for line in reader.readlines():
        words = line.split(',')
        activity = Activity(words[0], words[1], words[2], words[3])
        product = repo.products.find(Product(activity.product_id, 0, 0, 0))
        if float(activity.quantity) > 0:
            product.quantity = float(product.quantity) + float(activity.quantity)
            repo.products.update(product)
        if float(activity.quantity) < 0 and float(product.quantity) >= abs(float(activity.quantity)):
            product.quantity = float(product.quantity) + float(activity.quantity)
            repo.products.update(product)
        repo.activities.insert(activity)

import printdb