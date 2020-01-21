import os
from persistence import *


def main():
    print_all_tables()
    # employee_report()
    activity_report()


def print_all_tables():
    print("Activities")
    activities = repo.activities.find_all()
    for activity in activities:
        print("(" + str(activity.product_id) + ", " + str(activity.quantity) + ", " + str(
            activity.activator_id) + ", " + str(activity.date) + ")")
    print("Coffee stands")
    coffee_stands = repo.coffeeStands.find_all()
    for coffee_stand in coffee_stands:
        print("("+str(coffee_stand.id)+", "+coffee_stand.location+", "+str(coffee_stand.number_of_employees)+")")
    print("Employees")
    employees = repo.employees.find_all()
    for employee in employees:
        print("("+str(employee.id)+", "+employee.name+", "+str(employee.salary)+", "+str(+employee.coffee_stand)+")")
    print("Products")
    products = repo.products.find_all()
    for product in products:
        print("("+str(product.id)+", "+product.description+", "+str(product.price)+", "+str(product.quantity)+")")
    print("Suppliers")
    suppliers = repo.suppliers.find_all()
    for supplier in suppliers:
        print("("+str(supplier.id)+", "+supplier.name+", "+supplier.contact_information+")")


# def employee_report():
#     employee_income=repo.employee_income()
#     print("Employees report")
#     for item in employee_income:
#         print(item.name+" "+item.salary+" "+item.location+" "+item.income)


def activity_report():
    activity_with_name=repo.activity_with_name()
    print("Activities")
    for item in activity_with_name:
         print("("+str(item.date)+", "+item.description+", "+str(item.quantity)+", "+str(item.name_seller)+", "+str(item.name_supp)+")")