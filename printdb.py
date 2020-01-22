import os
from persistence import *

def print_all_tables():
    print("Activities")
    activities = repo.activities.find_all()
    for activity in activities:
        print("({}, {}, {}, {})".format(activity.product_id, activity.quantity, activity.activator_id, activity.date))
    print("Coffee stands")
    coffee_stands = repo.coffeeStands.find_all()
    for coffee_stand in coffee_stands:
        print("({}, '{}', {})".format(coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees))
    print("Employees")
    employees = repo.employees.find_all()
    for employee in employees:
        print("({}, '{}', {}, {})".format(employee.id, employee.name, employee.salary, employee.coffee_stand))
    print("Products")
    products = repo.products.find_all()
    for product in products:
        print("({}, '{}', {}, {})".format(product.id, product.description, product.price, product.quantity))
    print("Suppliers")
    suppliers = repo.suppliers.find_all()
    for supplier in suppliers:
        print("({}, '{}', '{}')".format(supplier.id, supplier.name, supplier.contact_information))


def employee_report():
    print("")
    print("Employees report")
    for employee in repo.employees.find_all():
        location=repo.coffeeStands.find(employee.coffee_stand)
        print("{}, {}, {}, {}".format(employee.name, employee.salary, repo.coffeeStands.find(employee.coffee_stand).location, repo.find_income(employee)))


def activity_report():
    activity_with_name=repo.activity_with_name()
    if len(activity_with_name) > 0:
        print("")
        print("Activities")
        for item in activity_with_name:
            print("({}, '{}', {}, '{}', '{}')".format(item.date, item.description, item.quantity, item.name_seller, item.name_supp))


# def main():
print_all_tables()
employee_report()
activity_report()