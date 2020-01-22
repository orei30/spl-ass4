import os
from persistence import *

def print_all_tables():
    print("Activities")
    activities = repo.activities.getToList()
    for activity in activities:
        print(activity)
    print("Coffee stands")
    coffee_stands = repo.coffeeStands.getToList()
    for coffee_stand in coffee_stands:
        print(coffee_stand)
    print("Employees")
    employees = repo.employees.getToList()
    for employee in employees:
        print(employee)
    print("Products")
    products = repo.products.getToList()
    for product in products:
        print(product)
    print("Suppliers")
    suppliers = repo.suppliers.getToList()
    for supplier in suppliers:
        print(supplier)

def employee_report():
    print("")
    print("Employees report")
    for employee in repo.employees.find_all():
        location=repo.coffeeStands.find(employee.coffee_stand)
        print("{} {} {} {}".format(employee.name, employee.salary, repo.coffeeStands.find(employee.coffee_stand).location, repo.find_income(employee)))


def activity_report():
    activity_with_name = repo.activity_with_name()
    if len(activity_with_name) > 0:
        print("")
        print("Activities")
        for item in activity_with_name:
            print(item)

print_all_tables()
employee_report()
activity_report()